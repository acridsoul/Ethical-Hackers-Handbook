from flask import Flask, render_template, request
import whois
from validator import is_registered

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        domain = request.form.get('domain', '').strip()
        try:
            if is_registered(domain):
                info = whois.whois(domain)
                result = {
                    'domain': domain,
                    'registrar': info.registrar,
                    'whois_server': info.whois_server,
                    'creation_date': info.creation_date,
                    'expiration_date': info.expiration_date,
                    'name_servers': info.name_servers
                }
            else:
                result = {'error': f'Domain {domain} is not registered'}
        except Exception as e:
            result = {'error': f'Lookup failed: {str(e)}'}
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)