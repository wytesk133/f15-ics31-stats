GRADES = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'P', 'NP', 'NR']

def read_from_file(path:str)->('x', 'y'):
    data = open(path)
    count = 0
    skipped = 0
    d = {}
    for line in data:
        l = line.split()
        letter_grade = l[1]
        if len(l) == 3:
            final = l[2]
        else:
            # probably did not go to final
            skipped += 1
            continue
        if letter_grade not in d:
            d[letter_grade] = []
        d[letter_grade].append(float(final))
        count += 1
    x = []
    y = []
    ordered = sorted(d.items(), key=lambda i: GRADES.index(i[0]))
    for item in ordered:
        key = item[0]
        value = item[1]
        x.append(key)
        y.append(value)
        print('{:2} => {}'.format(key, len(value)))
    data.close()
    print('Processed: {}/{}'.format(count, count + skipped))
    return x, y

def render():
    html = '''<!DOCTYPE html>
<html>
  <head>
    <title>ICS 31 Fall 2015 Grade Distribution</title>
    <meta charset="utf-8">
    <meta name="author" content="Waitaya Krongapiradee">
    <link rel="stylesheet" href="https://necolas.github.io/normalize.css/3.0.2/normalize.css">
    <script type="text/javascript" src="https://cdn.plot.ly/plotly-1.5.0.min.js"></script>
    <script type="text/javascript" src="http://numericjs.com/lib/numeric-1.2.6.min.js"></script>
  </head>
  <body>
    <div style="width: 80%; margin: auto">
        <div id="boxPlot"></div>
        <div id="gradeDistribution"></div>
    </div>
    <script type="text/javascript">
      var xData = {}
      var yData = {}

      var boxColor = []
      var allColors = numeric.linspace(0, 360, xData.length)
      for (var i = 0; i < xData.length; i++) {{
        boxColor.push('hsl(' + allColors[i] + ',50%' + ',50%)')
      }}

      var data1 = []
      var data2 = []

      for (var i = 0; i < xData.length; i++) {{
        var result = {{
          type: 'box',
          boxpoints: 'all',
          name: xData[i],
          y: yData[i],
          marker: {{
            color: boxColor[i]
          }}
        }}
        data1.push(result)
      }}

      var data2 = [
        {{
          x: xData,
          y: yData.map(y => {{
            return y.length
          }}),
          type: 'bar',
          marker: {{
            color: boxColor
          }}
        }}
      ]

      var layout1 = {{
        title: 'Grade vs Final Score'
      }}
      var layout2 = {{
        title: 'Grade Distribution'
      }}

      Plotly.newPlot('boxPlot', data1, layout1)
      Plotly.newPlot('gradeDistribution', data2, layout2)

      window.onresize = function() {{
        Plotly.Plots.resize(document.getElementById('boxPlot'))
        Plotly.Plots.resize(document.getElementById('gradeDistribution'))
      }}
    </script>
  </body>
</html>
'''
    output = open('index.html','w')
    x, y = read_from_file('ics_31_course_grades.txt')
    output.write(html.format(x, y))

if __name__ == '__main__':
    render()
