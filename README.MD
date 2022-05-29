<h1 align="center">Implementation of a TCP client-server to list the top-10 movies</h1>
<br>

## 💻 Challenge
Instructions:
- Download the MovieLens 1M database: [http://files.grouplens.org/datasets/movielens/ml-1m.zip](http://files.grouplens.org/datasets/movielens/ml-1m.zip)

- Install PySpark on your computer.

Specification:

Using PySpark, you must implement an algorithm that:

- Print the 10 films (one film per line) with the highest averages (in descending order) in the format: "<film name>, <average>"

- The average must be presented to two decimal places.

- You must simulate a generator (producer) of interactions (user, item and grade) and use Spark Streaming to consume and periodically update the top-10
  
- You can only use transformation functions like map*, reduce* to implement logic, where * indicates a suffix. For example, the reduceByKey function fits the reduce* pattern.

- You cannot use data frame or aggregate function.

- You can only use key-value pairs.

Reading suggestion:
- https://spark.apache.org/docs/latest/streaming-programming-guide.html
- https://medium.com/analytics-vidhya/apache-spark-structured-streaming-with-pyspark-b4a054a7947d
- https://www.infoq.com/br/articles/processamento-de-dados-apache-spark-2

</br>

## ⚒ Technologies used

-   **[Python](https://www.python.org/)**
-   **[Git](https://git-scm.com/)**
-   **[pySpark](https://spark.apache.org/docs/latest/api/python/)**
-   **[numpy](https://numpy.org/)**

Note: For a correct installation of Spark on the Windows operating system, I suggest following the [video](https://www.youtube.com/watch?v=WQErwxRTiW0).

</br>

## ⚒ Packages needed
- socket
- pickle
- time
- numpy
- os
- sys
- findspark
- SparkSession

</br>

## 🎮 Running the project
Open a command prompt, go to the file location and run the command:

```sh
produdor.py
```

Open a new prompt, go to the file location and run the command:
```sh
consumidor.py
```

</br>

## 📑 Report
The idea of the project is a system where a producer sends a certain amount of movie lines (in our case, 100 lines) from the movies.dat file to the consumer.

The connection established by the producer and consumer is made using the sockets library.

The consumer then processes these received lines to return the current top-10 of the most rated movies.

- More detailed information about the producer and consumer code is as comments inserted in the code of both.

</br>

---

### ✒️ Autor

</br>

<a href="https://github.com/gabriel61">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/gabriel61" width="100px;" alt=""/>
 <br />
 
 [![Linkedin Badge](https://img.shields.io/badge/-gabrielsampaio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/gabriel-oliveira-852759190/)](https://www.linkedin.com/in/gabriel-oliveira-852759190/)
<br>
sogabris@gmail.com
<br>

---

