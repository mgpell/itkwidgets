"""Viewer class

Visualization of an image.

In the future, will add optional segmentation mesh overlay.
"""

import ipywidgets as widgets
from traitlets import Unicode
from .trait_types import ITKImage, itkimage_serialization

@widgets.register
class Viewer(widgets.DOMWidget):
    """Viewer widget class."""
    _view_name = Unicode('ViewerView').tag(sync=True)
    _model_name = Unicode('ViewerModel').tag(sync=True)
    _view_module = Unicode('itk-jupyter-widgets').tag(sync=True)
    _model_module = Unicode('itk-jupyter-widgets').tag(sync=True)
    _view_module_version = Unicode('^0.10.2').tag(sync=True)
    _model_module_version = Unicode('^0.10.2').tag(sync=True)
    image = ITKImage(default_value=None, allow_none=True).tag(sync=True, **itkimage_serialization)

def view(image):
    """View the provided image."""
    viewer = Viewer(image=image)
    return viewer
