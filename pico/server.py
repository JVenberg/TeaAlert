from microWebSrv import MicroWebSrv


@MicroWebSrv.route('/token', 'POST')
def handlerWriteToken(httpClient, httpResponse):
    data = httpClient.ReadRequestContentAsJSON()
    if 'token' not in data:
        httpResponse.WriteResponseJSONError(400, {
            'status': 'error',
            'message': 'Must include "token" body param'
        })
    else:
        token_file = open('data/token', 'w')
        token_file.write(data['token'])
        token_file.close()
        httpResponse.WriteResponseJSONOk({
            'status': 'success',
            'message': 'Successfully wrote token'
        })


def run(threaded=False, port=8888, webPath='/www'):
    mws = MicroWebSrv(webPath=webPath)
    mws.Start(threaded=threaded)
