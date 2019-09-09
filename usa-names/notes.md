2019-08-08: when running "get_name_synonyms.py" overnight, got error on "madalyn"

```python
Traceback (most recent call last):
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py", line 472, in wrap_socket
    cnx.do_handshake()
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/OpenSSL/SSL.py", line 1915, in do_handshake
    self._raise_ssl_error(self._ssl, result)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/OpenSSL/SSL.py", line 1640, in _raise_ssl_error
    raise SysCallError(-1, "Unexpected EOF")
OpenSSL.SSL.SysCallError: (-1, 'Unexpected EOF')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/connectionpool.py", line 603, in urlopen
    chunked=chunked)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/connectionpool.py", line 344, in _make_request
    self._validate_conn(conn)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/connectionpool.py", line 843, in _validate_conn
    conn.connect()
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/connection.py", line 370, in connect
    ssl_context=context)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/util/ssl_.py", line 355, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py", line 478, in wrap_socket
    raise ssl.SSLError('bad handshake: %r' % e)
ssl.SSLError: ("bad handshake: SysCallError(-1, 'Unexpected EOF')",)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/connectionpool.py", line 641, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/urllib3/util/retry.py", line 399, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.behindthename.com', port=443): Max retries exceeded with url: /api/related.json?key=da105936325&name=madalyne (Caused by SSLError(SSLError("bad handshake: SysCallError(-1, 'Unexpected EOF')")))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "get_name_synonyms.py", line 10, in <module>
    dump_related_names(names, "data/name_synonyms.json")
  File "/home/david/Dropbox/Projects/100days-minis/usa-names/behindthename.py", line 39, in dump_related_names
    response = get_related_names(name)
  File "/home/david/Dropbox/Projects/100days-minis/usa-names/behindthename.py", line 31, in get_related_names
    response = call_api(f'{related_names_url}?key={API_KEY}&name={name}')
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/ratelimit/decorators.py", line 113, in wrapper
    return func(*args, **kargs)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/ratelimit/decorators.py", line 80, in wrapper
    return func(*args, **kargs)
  File "/home/david/Dropbox/Projects/100days-minis/usa-names/behindthename.py", line 19, in call_api
    response = requests.get(url)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/home/david/anaconda3/envs/usa-names/lib/python3.7/site-packages/requests/adapters.py", line 514, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='www.behindthename.com', port=443): Max retries exceeded with url: /api/related.json?key=da105936325&name=madalyne (Caused by SSLError(SSLError("bad handshake: SysCallError(-1, 'Unexpected EOF')")))
```