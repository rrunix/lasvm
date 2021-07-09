import numpy as np


def configuration(parent_package='', top_path=None):
    config = np.distutils.misc_util.Configuration('random', parent_package, top_path)

    config.add_extension('random_fast',
         sources=['random_fast.pyx', 'randomkit.c'],
         include_dirs=[np.get_include()]
         )

    return config

if __name__ == '__main__':
    np.numpy.distutils.core.setup(**configuration(top_path='').todict())
