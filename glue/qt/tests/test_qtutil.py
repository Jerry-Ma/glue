# pylint: disable=I0011,W0613,W0201,W0212,E1101,E1103

from __future__ import absolute_import, division, print_function

from mock import patch

from glue.external.qt import QtGui
from glue.core import Subset

from .. import qtutil


def test_glue_action_button():
    a = QtGui.QAction(None)
    a.setToolTip("testtooltip")
    a.setWhatsThis("testwhatsthis")
    a.setIcon(QtGui.QIcon("dummy_file"))
    a.setText('testtext')
    b = qtutil.GlueActionButton()
    b.set_action(a)

    # assert b.icon() == a.icon() icons are copied, apparently
    assert b.text() == a.text()
    assert b.toolTip() == a.toolTip()
    assert b.whatsThis() == a.whatsThis()

    #stays in sync
    a.setText('test2')
    assert b.text() == 'test2'


