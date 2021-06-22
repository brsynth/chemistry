"""A class to represent a chemical species."""
# The MIT License (MIT)
#
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
# Copyright (c) 2019 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from typing import (
    Dict,
)
from logging import (
    Logger,
    getLogger
)
from brs_utils import Cache
from chemlite.Object import Object


class Compound(Object):

    def __init__(
        self,
        id: str,
        smiles: str = '',
        inchi: str = '',
        inchikey: str = '',
        formula: str = '',
        name: str = '',
        logger: Logger = getLogger(__name__)
    ):
        super().__init__(
            id=id,
            logger=logger
        )
        self.set_smiles(smiles)
        self.set_inchi(inchi)
        self.set_inchikey(inchikey)
        self.set_formula(formula)
        self.set_name(name)
        Cache.add(self, self.get_id())

    ## OUT METHODS
    # def __repr__(self):
    #     return f'Compound {self.get_id()}'

    def _to_dict(self) -> Dict:
        '''
        Return a dictionary with all (with legacy) attributes of the object

        Returns
        -------
        obj_dict: Dict[str, TypeVar]
            A dictionary with all (with legacy) attributes
        '''
        return {
            **super()._to_dict(),
            **self.__to_dict()
        }

    def __to_dict(self) -> Dict:
        '''
        Return a dictionary with (specific) attributes

        Returns
        -------
        obj_dict: Dict[str, TypeVar]
            A dictionary with (specific) attributes of the object
        '''
        return {
            'name': self.get_name(),
            'smiles': self.get_smiles(),
            'inchi': self.get_inchi(),
            'inchikey': self.get_inchikey(),
            'formula': self.get_formula(),
        }

    ## READ METHODS
    def get_name(self) -> str:
        return self.__name

    def get_smiles(self) -> str:
        return self.__smiles

    def get_inchi(self) -> str:
        return self.__inchi

    def get_inchikey(self) -> str:
        return self.__inchikey

    def get_formula(self) -> str:
        return self.__formula

    ## WRITE METHODS
    def set_name(self, name: str) -> None:
        self.__name = name

    def set_smiles(self, smiles: str) -> None:
        self.__smiles = smiles

    def set_inchi(self, inchi: str) -> None:
        self.__inchi = inchi

    def set_inchikey(self, inchikey: str) -> None:
        self.__inchikey = inchikey

    def set_formula(self, formula: str) -> None:
        self.__formula = formula
