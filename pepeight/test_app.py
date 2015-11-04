import pytest
from django.core.urlresolvers import reverse_lazy


@pytest.mark.django_db
def test_can_get(client):
    resp = client.get(reverse_lazy('home'))
    assert "pep8" in resp.content

@pytest.mark.parametrize("mode", ["0",'1','2'])
@pytest.mark.django_db
def test_can_post(mode,client):
    data=r"""import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)"""
    resp = client.post(reverse_lazy('home'),{"code":data,"mode":mode})
    assert not ";" in resp.content

