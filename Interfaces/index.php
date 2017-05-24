<html>
	<head>
	<title>Red neuronal</title>
		<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
		<link rel='stylesheet' type='text/css' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'>
	</head>

	<style>
	#header {
	    text-align:center;
        padding:10px;
    }
    </style>
	<body background="resources/fondob.jpg">
	    <div id="header">
        <h1>
            <font face="arial black" size="10" color=#0B173B>REDES</font>
            <font face="arial black" size="10" color=#122A0A>NEURONALES</font>
        </h1>
        </div>
		<div class="container">
			<?php
			$servername = "localhost";
			$username = "user";
			$password = "user1234";
			$dbname = "Neural_Network";
			$conn = new mysqli($servername, $username, $password, $dbname);
			
			if ($conn->connect_error) {
			    die("Connection failed: " . $conn->connect_error);
			}

			$sql = "SELECT * FROM ejecucion";
			$result = $conn->query($sql);

			if ($result->num_rows > 0) {
			    echo "<table class='table table-bordered'> 
			    		<tr> 
			    		<th>ID</th>
			    		<th>Capas</th>
			    		<th>Neuronas</th>
			    		<th>Lambda</th>
			    		<th>Costo Inicial</th>
			    		<th>% Precision Training</th>
			    		<th>% Precision Test</th>
			    		<th>% Error Training</th>
			    		<th>% Error Test</th>
			    		</tr>";
			    // output data of each row
			    while($row = $result->fetch_assoc()) {
			        echo "<tr>
			        	<td>".$row["id"]."</td>
			        	<td>".$row["capas"]."</td>
			        	<td>".$row["neuronas"]."</td>
			        	<td>".$row["lambda"]."</td>
			        	<td>".$row["costo_inicial"]."</td>
			        	<td>".$row["precision_training"]."</td>
			        	<td>".$row["precision_test"]."</td>
			        	<td>".$row["error_training"]."</td>
			        	<td>".$row["error_test"]."</td>
			        	</tr>";
			    }
			    echo "</table>";
			} else {
			    echo "0 results";
			}
			$conn->close();
			?>
		</div>

	</body>
</html>
