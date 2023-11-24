try:
    import json
    from websockets.sync.client import connect, ClientConnection
    from PIL import Image
    import requests
    import io
except:
    import os
    os.system('pip install websockets')
    os.system('pip install PIL-Tools')
