$(document).ready(function () {
    $('#headActive li a').each(function () {
        var location = window.location.href;
        var link = this.href;
        if (location == link) {
            $(this).addClass('active');
        }
    });
});


  var spis = document.getElementsByClassName('conName').length;
  var conName = document.getElementsByClassName("conName");
  var result = document.getElementsByClassName('result');
  console.log(conName);
  var conArray = [['Name', 'result']];
    for (var i = 0; i < spis; i++) {
      conArray.push([conName[i].textContent, Number(result[i].textContent)]);
    };     
    console.log(conArray);
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = google.visualization.arrayToDataTable(conArray);

      var options = {
		is3D: true,
      };

      var chart = new google.visualization.PieChart(document.getElementById('piechart'));

      chart.draw(data, options);
    };

		(function (document, window, index){
			'use strict';
			var inputs = document.querySelectorAll('.inputImage');
			Array.prototype.forEach.call(inputs, function (input) {
				var label = input.nextElementSibling,
						labelVal = label.innerHTML;

				input.addEventListener('change', function (e) {
					var fileName = '';
					if (this.files && this.files.length > 1)
						fileName = ( this.getAttribute('data-multiple-caption') || '' ).replace('{count}', this.files.length);
					else
						fileName = e.target.value.split('\\').pop();

					if (fileName)
						label.querySelector('span').innerHTML = fileName;
					else
						label.innerHTML = labelVal;
				});

				// Firefox bug fix
				input.addEventListener('focus', function () {
					input.classList.add('has-focus');
				});
				input.addEventListener('blur', function () {
					input.classList.remove('has-focus');
				});
			});
		}(document, window, 0));

