<html>
	<head>
	<title>Red neuronal</title>
		<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
		<link rel='stylesheet' type='text/css' href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'>
	</head>

	<body>

		<div class="container">
			<h1>Redes Neuronales</h1>
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
			    		<th>Curva aprendizaje</th>
			    		<th>Costo</th>
			    		<th>Error</th>
			    		</tr>";
			    // output data of each row
			    while($row = $result->fetch_assoc()) {
			        echo "<tr>
			        	<td>".$row["id"]."</td>
			        	<td>".$row["capas"]."</td>
			        	<td>".$row["neuronas"]."</td>
			        	<td>".$row["curva_aprendizaje"]."</td>
			        	<td>".$row["costo"]."</td>
			        	<td>".$row["error"]."</td>
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