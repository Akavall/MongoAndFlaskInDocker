Run build ther services:

```
sudo docker-compose up --build
```

`--build` is not required, but guarantees that services are rebuild.

Call the service from python shell:

```
import requests

result = requests.post("http://localhost:8000/add_up", data={"a": 107, "b": 89})
```

Result should be something like this:

```
In [15]: result.content
Out[15]: '{"answer": "196"}'
```
