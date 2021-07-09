import os.path
import numpy as np

extra_compile_args = ['-O3', '-ffast-math', '-march=native', '-fopenmp']
extra_link_args=['-fopenmp']

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('lasvm', parent_package, top_path)

    randomdir = os.path.join(top_path, "lasvm", "random")

    config.add_extension('dataset_fast',
         sources=['dataset_fast.pyx'],
         include_dirs=[np.get_include(), randomdir],
         extra_compile_args=extra_compile_args,
         extra_link_args=extra_link_args
         )

    config.add_extension('lasvm_fast',
         sources=['lasvm_fast.pyx'],
         include_dirs=[np.get_include(), randomdir],
         extra_compile_args=extra_compile_args,
         extra_link_args=extra_link_args
         )


    config.add_extension('select_fast',
         sources=['select_fast.pyx'],
         include_dirs=[np.get_include(), randomdir],
         extra_compile_args=extra_compile_args,
         extra_link_args=extra_link_args
         )

    config.add_subpackage('random')
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
