def read_from_file(path:str)->str:
    data = open(path)
    result = ''
    count = 0
    first = 1
    for line in data:
        l = line.split()
        if len(l) != 3:
            # probably did not go to final
            continue
        letter_grade = l[1]
        final = l[2]
        if letter_grade == 'A+':
            grade = 4
        elif letter_grade == 'A':
            grade = 4
        elif letter_grade == 'A-':
            grade = 3.7
        elif letter_grade == 'B+':
            grade = 3.3
        elif letter_grade == 'B':
            grade = 3
        elif letter_grade == 'B-':
            grade = 2.7
        elif letter_grade == 'C+':
            grade = 2.3
        elif letter_grade == 'C':
            grade = 2
        elif letter_grade == 'C-':
            grade = 1.7
        elif letter_grade == 'D+':
            grade = 1.3
        elif letter_grade == 'D':
            grade = 1
        elif letter_grade == 'D-':
            grade = 0.7
        elif letter_grade == 'F':
            grade = 0
        elif letter_grade == 'P':
            # cannot assume their grades
            continue
        elif letter_grade == 'NP':
            # cannot assume their grades
            continue
        elif letter_grade == 'NR':
            # cannot assume their grades
            # probably cheated
            continue
        if not first:
            result += ','
        first = 0
        result += '[%s,%s]' % (grade, final)
        count += 1
    print('Count: %d' % count)
    return result

def render():
    html = '''<!DOCTYPE html>
<html>
  <head>
    <title>ICS 31 Fall 2015 Grade Distribution</title>
    <meta charset="utf-8">
    <meta name="author" content="Waitaya Krongapiradee">
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Grade', 'Final Score'],
          %s
        ]);

        var options = {
          title: 'Grade vs. Final Score Comparison',
          hAxis: {title: 'Grade', minValue: 0, maxValue: 4},
          vAxis: {title: 'Final Score', minValue: 0, maxValue: 70},
          legend: 'none'
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>
'''
    output = open('index.html','w')
    output.write(html % read_from_file('ics_31_course_grades.txt'))

if __name__ == '__main__':
    render()
