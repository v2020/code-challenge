from typing import Dict

from flask import Flask, render_template, request, url_for

from project.utils import CountBox

from .utils import DashboardUtils, FilterForm, TableUtils, VulnerabilityDataJson


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    @app.route("/")
    def dashboard():
        # Dashboard with counters and graphs
        data_file: str = app.config["DATA_FILE"]
        vutils: DashboardUtils = DashboardUtils(VulnerabilityDataJson(data_file))

        # TODO: Graphs data processing/render needs refactoring
        graph_data1: Dict[str, int] = vutils.get_statistic_by_name("category")
        graph_data2: Dict[str, int] = vutils.get_statistic_by_name("impact")
        graph_data3: Dict[str, int] = vutils.get_statistic_by_name("type")

        counts: list[CountBox] = vutils.get_counts()
        template_name: str = "pages/dashboard.html"
        return render_template(
            template_name,
            graph_data1=graph_data1,
            graph_data2=graph_data2,
            graph_data3=graph_data3,
            counts=counts,
        )

    @app.route("/vulnerabilities/")
    def vulnerabilities():
        # Output a table listing all the vulnerabilities
        sort = request.args.get("sort", None)
        data_file: str = app.config["DATA_FILE"]
        table_item: TableUtils = TableUtils(VulnerabilityDataJson(data_file), request)
        table_header = table_item.get_table_header(sort)
        vulnerability_list = table_item.get_table(sort)
        form = table_item.get_form()
        template_name = "pages/vulnerability_list.html"
        return render_template(
            template_name,
            vulnerability_list=vulnerability_list,
            vulnerability_header=table_header,
            form=form,
        )

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def page_not_found(error):
        return render_template("500.html"), 500

    return app
