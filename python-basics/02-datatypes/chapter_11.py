import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()

brewing_time.to("Europe/Rome")

chai_profil = namedtuple("ChaiProfile", ["flavor", "aroma"])
