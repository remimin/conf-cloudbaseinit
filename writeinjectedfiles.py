import os
from oslo_log import log as oslo_logging

from cloudbaseinit.plugins.common import base


LOG = oslo_logging.getLogger(__name__)
DEFAULT_PERMISSIONS = 0o644


class WriteInjectedFiles(base.BasePlugin):

    def execute(self, service, shared_data):
        if hasattr(service, 'get_injected_files'):
            for path, content in service.get_injected_files():
                LOG.info("Inject file %s" %path)
                dirname = os.path.dirname(path)
                if not os.path.isdir(dirname):
                    try:
                        os.makedirs(dirname)
                    except OSError as exc:
                        LOG.exception(exc)
                        continue
                with open(path, "wb") as file_handle:
                    file_handle.write(content)
                    file_handle.flush()
                os.chmod(path, DEFAULT_PERMISSIONS)

        return base.PLUGIN_EXECUTION_DONE, False
