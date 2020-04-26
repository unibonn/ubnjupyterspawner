from jinja2 import Template
from tornado.log import app_log

from .formspawners import ParamForm


class NDForm(ParamForm):

    source = 'static/ndform.html'

    def parse_options(self, formdata):
        data = super().parse_options(formdata)
        intsettings = {'req_memory', 'req_nprocs', 'req_ngpus'}
        data = {k: int(v) if v in intsettings else v for k, v in data.items()}
        data['req_runtime'] = '{runtime}:00'.form(runtime=data['req_runtime'])
        return data

    def generate(self):
        app_log.info("Generating form from: %s", self)
        return Template(super().generate()).render()
