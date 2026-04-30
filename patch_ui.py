import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# result-card -> glass-card Tailwind panel
html = re.sub(r'class="result-card [^"]*"', 'class="glass-card rounded-xl p-5 hover:border-primary/30 hover:-translate-y-1 transition-all"', html)

# section panels - add Tailwind glass wrapper
for cls in ['risk-section','ndvi-timeline-section','ndvi-section','disease-section','charts-section','advisory-section','mandi-section','disaster-section','chat-section','news-section','report-section']:
    html = re.sub(r'class="' + cls + '"', 'class="glass-card rounded-xl p-5 space-y-4 ' + cls + '"', html)

# section-header
html = re.sub(r'class="section-header"', 'class="flex items-center gap-3 mb-2"', html)

# card typography
html = re.sub(r'class="card-value"', 'class="text-2xl font-bold font-data-mono text-primary leading-tight mb-1"', html)
html = re.sub(r'class="card-detail"', 'class="text-xs text-on-surface-variant"', html)
html = re.sub(r'class="card-header"', 'class="flex items-center gap-2 mb-3 flex-wrap"', html)
html = re.sub(r'class="card-icon"', 'class="text-xl"', html)

# modal-content
html = re.sub(r'class="modal-content glass-card-high"', 'class="glass-card-high rounded-2xl w-full max-w-lg max-h-[80vh] overflow-y-auto"', html)

# charts-grid
html = re.sub(r'class="charts-grid"', 'class="grid grid-cols-1 lg:grid-cols-2 gap-4"', html)
html = re.sub(r'class="chart-card"', 'class="bg-surface-container/50 border border-outline-variant/40 rounded-xl p-4"', html)
html = re.sub(r'class="chart-card ndvi-timeline-card"', 'class="bg-surface-container/50 border border-outline-variant/40 rounded-xl p-4"', html)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
