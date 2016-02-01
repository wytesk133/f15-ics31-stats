GRADES = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'P', 'NP', 'NR']

def extract_final(path:str)->('x', 'y'):
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
    data.close()
    print('Processed: {} (Skipped: {})'.format(count, skipped))
    return x, y

def extract_midterm(path:str)->('x', 'y'):
    data = open(path)
    x = []
    y = []
    count = 0
    skipped = 0
    for line in data:
        l = line.replace('[', ' ').replace(']', ' ').split()
        if(l[0][-1] == '-'):
            skipped += int(l[1])
            continue
        x.append(int(float(l[0])))
        y.append(int(l[1]))
        count += int(l[1])
    x.reverse()
    y.reverse()
    data.close()
    print('Processed: {} (Skipped: {})'.format(count, skipped))
    return x, y

def render():
    html = '''<!DOCTYPE html>
<html>
  <head>
    <title>ICS 31 Fall 2015 Statistics</title>
    <meta charset="utf-8">
    <meta name="author" content="Waitaya Krongapiradee">
    <link rel="stylesheet" href="https://necolas.github.io/normalize.css/3.0.2/normalize.css">
    <script type="text/javascript" src="https://cdn.plot.ly/plotly-1.5.0.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.min.js"></script>
  </head>
  <body>
    <div style="max-width: 1024px; margin: auto">
        <div id="boxPlot"></div>
        <div id="gradeDistribution"></div>
        <div id="midterm1"></div>
        <div id="midterm2"></div>
    </div>
    <script type="text/javascript">
      'use strict'

      var finalGrades = {}
      var finalData = {}
      var midterm1Score = {}
      var midterm1Count = {}
      var midterm2Score = {}
      var midterm2Count = {}

      var data1 = []
      var data2 = []
      var data3 = []
      var data4 = []

      function generate_rainbow (n) {{
        var allColors = numeric.linspace(0, 360, n)
        var result = []
        for (var i = 0; i < n; i++) {{
          result.push('hsl(' + allColors[i] + ',50%' + ',50%)')
        }}
        return result
      }}

      var rainbow = generate_rainbow(finalGrades.length)

      for (var i = 0; i < finalGrades.length; i++) {{
        var result = {{
          type: 'box',
          boxpoints: 'all',
          name: finalGrades[i],
          y: finalData[i],
          marker: {{
            color: rainbow[i]
          }}
        }}
        data1.push(result)
      }}

      var data2 = [
        {{
          x: finalGrades,
          y: finalData.map(y => {{
            return y.length
          }}),
          type: 'bar',
          marker: {{
            color: rainbow
          }}
        }}
      ]

      rainbow = generate_rainbow(midterm1Score.length)

      var data3 = [
        {{
          x: midterm1Score,
          y: midterm1Count,
          type: 'bar',
          marker: {{
            color: rainbow
          }}
        }}
      ]

      rainbow = generate_rainbow(midterm2Score.length)

      var data4 = [
        {{
          x: midterm2Score,
          y: midterm2Count,
          type: 'bar',
          marker: {{
            color: rainbow
          }}
        }}
      ]

      var layout1 = {{
        title: 'Grade vs Final Score'
      }}
      var layout2 = {{
        title: 'Grade Distribution'
      }}
      var layout3 = {{
        title: 'First Midterm Score Distribution'
      }}
      var layout4 = {{
        title: 'Second Midterm Score Distribution'
      }}

      Plotly.newPlot('boxPlot', data1, layout1)
      Plotly.newPlot('gradeDistribution', data2, layout2)
      Plotly.newPlot('midterm1', data3, layout3)
      Plotly.newPlot('midterm2', data4, layout4)

      window.onresize = function() {{
        Plotly.Plots.resize(document.getElementById('boxPlot'))
        Plotly.Plots.resize(document.getElementById('gradeDistribution'))
        Plotly.Plots.resize(document.getElementById('midterm1'))
        Plotly.Plots.resize(document.getElementById('midterm2'))
      }}
    </script>
  </body>
</html>
'''
    output = open('index.html','w')
    x_f, y_f = extract_final('ics_31_course_grades.txt')
    x_m1, y_m1 = extract_midterm('f15.mt1.stats.txt')
    x_m2, y_m2 = extract_midterm('f15.mt2.stats.txt')
    output.write(html.format(x_f, y_f, x_m1, y_m1, x_m2, y_m2))

if __name__ == '__main__':
    render()
