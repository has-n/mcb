import os

from config import data_path
from utils.utils import make_dir


class MatlabAPI:
    def __init__(self):
        import matlab.engine
        self.eng = matlab.engine.start_matlab()
        self.eng.addpath(r'utils/mat_files', nargout=0)

    def make_image(self, obj_dir, output_dir=None):
        if not output_dir:
            output_dir = os.path.join(data_path, 'image', *obj_dir.split('/')[-2:])
        make_dir(output_dir)
        self.eng.render_SHREC(obj_dir, output_dir, nargout=0)

    def close(self):
        self.eng.exit()
