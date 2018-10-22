from __future__ import absolute_import, division, print_function, unicode_literals

from .gp import GP


class AbstractVariationalGP(GP):
    def __init__(self, variational_strategy):
        super(AbstractVariationalGP, self).__init__()
        self.variational_strategy = variational_strategy

    def forward(self, x):
        raise NotImplementedError

    def __call__(self, inputs, **kwargs):
        return self.variational_strategy(inputs)
