GRADES = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'P', 'NP', 'NR']

def read_from_file(path:str)->('x', 'y'):
    data = open(path)
    count = 0
    d = {}
    for line in data:
        l = line.split()
        letter_grade = l[1]
        if len(l) == 3:
            final = l[2]
        else:
            # probably did not go to final
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
    print('Processed: %d' % count)
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
    <div id="myDiv" style="width: 900px; height: 500px;"></div>
    <script type="text/javascript">
      var xData = %s
      var yData = %s

      var boxColor = []
      var allColors = numeric.linspace(0, 360, xData.length)
      for (var i = 0; i < xData.length; i++) {
        boxColor.push('hsl('+ allColors[i] +',50%%'+',50%%)')
      }

      var data = []

      for (var i = 0; i < xData.length; i++) {
        var result = {
          type: 'box',
          name: xData[i],
          y: yData[i],
          marker: {
            color: boxColor[i]
          }
        }
        data.push(result)
      }

      var layout = {
        title: 'Grade vs Final Score',
        width: window.innerWidth,
        height: window.innerHeight
      }

      Plotly.newPlot('myDiv', data, layout)
    </script>
  </body>
</html>
'''
    output = open('index.html','w')
    output.write(html % read_from_file('ics_31_course_grades.txt'))

if __name__ == '__main__':
    render()
