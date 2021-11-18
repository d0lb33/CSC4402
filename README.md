## CSC4402 Project
### By: Jonathan Dolbee, Ryan Bourdais, Christian Cox
-------------
  

1.  The CSC4402 project is a group project. The students should form groups each of which consists of **4 to 5** people. Each group will work as an entity to produce one ﬁnal result for the project. Each group should work independently-NO collaboration between groups is allowed.
 
2.  The implementation can be done on the using relational database system MYSQL or SQLite. If you would like to develop a more complex database application with GUI and Web access, you may use a different computer/database platform. However, you should inform the CSC4402 instructor about your choice of platform/project format.

3. The task for the project is to design and implement a relational database application for a suitable (real world or prototype) application domain. The project should contain the following components.
 
	<ol type="a">
	  <li>Domain Application. You should understand the nature of the application, the entities important to the application, the specific attributes to be stored in the database, the relationship among the entities (and among the attributes), the constraints imposed on the database (attributes) by the nature of applications, the assumptions made by the database designer. The result of this step should be an entity-relationship model (E-R diagram) of the application, plus a list of constraints and assumptions.</li>
	  <li>Database Design. You should decide the table structures of the database: How many tables should we have? What are the attributes (columns) in each table? What are the primary key and the foreign keys. Whether the tables are in some desired normal form? The theory of logical design of relational databases will be used in this phase. The result of this step should be in the form of table schemes (relational schemes) such that each table is in some desired normal form.</li>
	  <li>Create the database, gather sample data and insert them to the database. Design queries and implement them using SQL to get data statistics. The SQL query should be presented, followed by the screenshot of the resulting records.</li>
	  <li>Write up a report, describing the above process (a) - (c), including the script of pro-gram execution and program source code, with appropriate documentations. Finally, present the summary of the project in class. It is expected that every member of the group will participate in the presentation.</li>
	  <li>The database designed should contain at least **3** entities, **2** relationships, each with a few attributes. The database should have a reasonably rich structure (e.g., one-to-many relationship) to allow interesting queries. Each table should have at least **100** records, because otherwise most of your queries will return no records. Your project should include **10** SQL "select" queries. You should design interesting queries to utilize the SQL skills (join queries, sub-queries, use of "group by" and aggregation functions, etc.)</li>
	</ol>



## Final presentation:

  

### Goal and Motivation:

  

### Brief overview of the problem:

  

### Data:
*Where did you got it? Size? Format?*
We got the data from an iTunes library export of data seen in the songs.csv file.
It is 48.8KB of data.
**Data Sample:**
|song_name                                    |time|album_name                                       |genre      |release_date|album_artist                 |
|---------------------------------------------|----|-------------------------------------------------|-----------|------------|-----------------------------|
|MagSafe                                      |2:10|MagSafe - Single                                 |Pop        |11/12/2020  |Jonathan & Friends & Wolf    |
|Wanted                                       |2:16|Human (Deluxe)                                   |Pop        |9/9/2019    |OneRepublic                  |
|MONTERO (Call Me By Your Name)               |2:18|MONTERO (Call Me By Your Name) - Single          |Pop        |3/26/2021   |Lil Nas X                    |
|my ex's best friend                          |2:19|Tickets to My Downfall (SOLD OUT Deluxe)         |Alternative|8/7/2020    |Machine Gun Kelly            |
|oops!                                        |2:20|Gasanova                                         |Hip-Hop/Rap|10/2/2020   |Yung Gravy                   |
|Mood (feat. iann dior)                       |2:21|El Dorado                                        |Hip-Hop/Rap|7/24/2020   |24kGoldn                     |
|STAY                                         |2:22|STAY - Single                                    |Pop        |7/9/2021    |The Kid LAROI & Justin Bieber|
|THATS WHAT I WANT                            |2:24|MONTERO                                          |Pop        |9/17/2021   |Lil Nas X                    |
|if we never met (feat. Kelsea Ballerini)     |2:24|if we never met (feat. Kelsea Ballerini) - Single|Pop        |10/9/2020   |John K                       |
|Body Language                                |2:25|Good Things                                      |Country    |8/13/2021   |Dan + Shay                   |
|Drip Too Hard                                |2:26|Drip Harder                                      |Hip-Hop/Rap|9/12/2018   |Lil Baby & Gunna             |
|Screaming Underwater                         |2:26|Screaming Underwater - Single                    |Pop        |9/10/2021   |Alex Warren                  |
|Just Drive                                   |2:28|Just Drive - Single                              |Country    |8/6/2021    |Erin Kinsey                  |

  

### Your approaches:

  

### Database Design and Management (ER, normalization, etc.):

  

### Your experimental results and Conclusions:

  

### Querying and Data statistics:

  

### What did you learn?

  

## Final project report:
  
1.  **Writeup**: Describe in depth the answers of the previous question 3a to 3e.

1.  **Software**: packaging, documentation, and portability. The goal is to provide enough material, so that other people can use it. Create a zip file of the code and a short **README.txt** file. This file should describe the package in a few paragraphs, how to use it, and how to run a demo (if any).

