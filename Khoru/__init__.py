import os
import logging
from logging import handlers

__file = "sayu.log"
__dr = "./logs/"
if not os.path.exists(__dr):
    os.makedirs(__dr)
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING,
                    handlers=[
                        handlers.RotatingFileHandler(
                            filename=__dr + __file,
                            maxBytes=3145728,
                            backupCount=1
                        ),
                        logging.StreamHandler()
                    ]
                    )
sayulog = logging.getLogger("KhoruBot")
