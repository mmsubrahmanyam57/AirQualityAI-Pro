from flask import Flask, render_template, request, jsonify, Response
from pollution_model import simulate
import csv,io,time,math
app=Flask(__name__)
def result():
    speed,direction,emission=[float(request.args.get(k,v)) for k,v in [('speed',14),('direction',0),('emission',70)]]
    source=int(request.args.get('source',0))
    if not all(map(math.isfinite,[speed,direction,emission])) or not (2<=speed<=30 and 0<=direction<360 and 10<=emission<=100 and 0<=source<3): raise ValueError('Invalid settings')
    return simulate(speed,direction,emission,source)
@app.route('/')
def index():return render_template('index.html')
@app.route('/api/simulate')
def api():
    try:return jsonify(result())
    except (ValueError,IndexError,OverflowError):return jsonify(error='Invalid simulation settings'),400
@app.route('/report.csv')
def report():
    try: rows=result()['sensors']
    except (ValueError,IndexError,OverflowError):return 'Invalid settings',400
    f=io.StringIO(); w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
    return Response(f.getvalue(),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=demo-sensor-report.csv'})
@app.route('/monitor')
def monitor():return render_template('monitor.html')
@app.route('/api/health')
def health():return jsonify(status='ok',engine='Monte Carlo backward particle search',sensors=12,particles_per_sensor=80,steps_per_particle=45,mode='synthetic',storage='none')
@app.route('/api/diagnostics')
def diagnostics():
    start=time.perf_counter(); d=simulate(); elapsed=round((time.perf_counter()-start)*1000,1)
    return jsonify(status='ok',elapsed_ms=elapsed,sensor_count=len(d['sensors']),trajectory_count=len(d['paths']),score_total=round(sum(s['score'] for s in d['sources']),2),top_source=d['sources'][0]['name'],sample_sensor=d['sensors'][0])
if __name__=='__main__':app.run(port=5000)
