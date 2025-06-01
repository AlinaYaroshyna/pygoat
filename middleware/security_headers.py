def security_headers(get_response):
    def middleware(request):
        response = get_response(request)
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Content-Security-Policy'] = "default-src 'self'"
        response['Referrer-Policy'] = 'no-referrer'
        return response
    return middleware
