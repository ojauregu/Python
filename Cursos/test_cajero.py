
from cajero2 import cajero

def test_cajero():
    d= {100:{100:1},250:{200:1,50:1},300:{200:1,100:1}}
    for impo,billetes in d.items():
        result=cajero(impo)
        assert result ==billetes
