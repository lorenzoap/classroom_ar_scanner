





	




Classroom Scanner AR







Titolo progetto:  Classroom Scanner AR
Alunno/i: 	     Julian Sprugasci
     Lorenzo Piazza, 
     Pierpaolo Casati e 
     Claudio Engeler
Classe: 	     Info 3
Anno scolastico: 2019/2020
Responsabile:     Geo Petrini


1.	Introduzione

1.1	   Informazioni sul progetto	
Allievi coinvolti: Julian Sprugasci, Lorenzo Piazza, Pierpaolo Casati e Claudio Engeler
Classe: Informatica 3AC presso la SAM Trevano
Docente responsabile: Geo Petrini
Data inizio: 2019/01/17
Data fine: 08.05.2020

1.2	   Abstract

A school needs a system capable of managing lesson times and various classrooms. This project aims to create an augmented reality system, which through the QR codes present in the classrooms will make the time of day of that single classroom appear to improve research and facilitate people. It will also be possible to search for a classroom through a GPS function. To do this we will use the notions learned in our school using the following languages:
sql, php, css, js and html.

1.3	   Scopo

Questo progetto ha lo scopo didattico principale di imparare a gestire in team un progetto IT e di prepararci per l’esame di fine tirocinio. Per fare ciò dobbiamo ricorrere a tutte nozioni apprese durante la nostra formazione, utilizzando molti aspetti visti in varie materie, come per esempio la creazione e gestione di un Gantt oppure l’utilizzo di vari linguaggi di programmazione. L'altro scopo di questo progetto sarà quello di creare un applicativo che permetta di gestire l’orario scolastico della nostra sezione attraverso la realtà aumentata. Tutto il lavoro verrà suddiviso equamente all’interno del nostro team di lavoro per spartirci bene i compiti e svolgere al meglio il progetto.


2.	Analisi

2.1	   Analisi del dominio

Il docente supervisore che ci ha stipulato le specifiche del progetto è dalla parte del cliente e ci ha assegnato un diario dei compiti. Il risultato finale, come spiegato nelle specifiche dovrà essere un applicativo web che dovrà gestire gli orari della nostra sezione e dare la possibilità alle persone di guardare l’orario in maniera immediata e più semplice attraverso la loro telecamera del telefono. L’applicativo sarà implementato in html, css, js e python. Il tutto sarà caricato su un web server di Github e quindi sarà facilmente accessibile da tutti coloro che hanno un browser web adeguato (Firefox, Chrome e Safari).
Questo prodotto non esiste ancora sul mercato ma non verrà progettato per scopi lucrativi ma solamente a scopo didattico per consolidare le nostre nozioni. All’inizio del piano della nostra sezione scolastica avrà un codice QR che corrisponderà al piano corrente. Poi in ogni aula del quarto piano sarà presente un codice QR con un pattern univoco per distinguerle, che una volta scannerizzato mostrerà a schermo l’orario della lezione in corso. Mentre se si volessero avere più informazioni riguardanti quell’aula si potrà premere sul popup a schermo che porterà direttamente ad una pagina web con tutte le informazioni necessarie. Tutte le specifiche e la guida su come utilizzare il prodotto sarà presente sul nostro sito.

2.2	   Analisi e specifica dei requisiti 

ID: REQ-001
Nome	Realizzare un sito web per l’applicativo
Priorità	1
Versione	1.0
Categoria	Linguaggio
Sotto Requisiti
001	Il sito deve essere adatto per qualsiasi dispositivo
002	Deve esserci una guida utente
003	Il sito dovrà essere indipendente
004	L’interfaccia e i colori di sfondo dovranno essere adatti a qualsiasi utente 

ID: REQ-002
Nome	Dovrà essere presente un QR Code per il quarto piano
Priorità	2
Versione	1.0
Categoria	Sistema
Sotto Requisiti
001	Il QR Code avrà un colore di sfondo particolare per essere distinto
002	Il QR Code dovrà portare direttamente al nostro sito web

ID: REQ-003
Nome	Ogni aula dovrà avere un pattern univoco per essere riconosciuta
Priorità	2
Versione	1.0
Categoria	Sistema
Sotto Requisiti
001	Il pattern non dovrà avere delle forme complesse



ID: REQ-004
Nome	L’applicativo dovrà avere la funzione di lettura dei pattern
Priorità	1
Versione	1.0
Categoria	Sistema e Linguaggio
Sotto Requisiti
001	Lo scanner dovrà essere eseguito attraverso la fotocamera del dispositivo
002	Dovrà essere in grado di riconoscere tutti i pattern assegnati alle aule
003	Una volta proiettato il risultato dovrà essere possibile cliccare sul popup per mostrare delle informazioni in più riguardanti l’orario
004	L’interfaccia e i colori di sfondo dovranno essere adatti a qualsiasi utente 

       
ID: REQ-005
Nome	L’applicativo dovrà mostrare gli orari in AR
Priorità	1
Versione	1.0
Categoria	Linguaggio
Sotto Requisiti
001	Bisogna creare un finestra popup uguale per tutte le aule
002	Dovrà essere possibile leggere il database e estrarre l’orario corrente
003	Dovrà esserci la funzione “Maggiori informazioni”
004	Bisogna mostrare gli orari da qualsiasi angolazione si legge il QR Code

    
ID: REQ-006
Nome	L’applicativo dovrà avere un database con tutti gli orari
Priorità	1
Versione	1.0
Categoria	Linguaggio e Sistema
Sotto Requisiti
001	Il database dovrà essere aggiornato una volta ogni anno
002	Il database deve contenere tutti i dati riguardanti gli orari
003	Il database dovrà essere sempre attivo durante i giorni lavorati
004	Il database sarà sviluppato il MySQL e caricato su un server


ID: REQ-007
Nome	Bisogna creare uno script in grado di estrarre i dati dal sito dell’orario
Priorità	1
Versione	1.0
Categoria	Linguaggio
Sotto Requisiti
001	Lo script verrà sviluppato il Python e Flask
002	Dovrà essere in grado di estrarre i dati e inserirli nel database
003	Dovrà essere eseguito una volta all’anno per aggiornare i dati 





ID: REQ-008
Nome	L’applicativo dovrà avere un sistema per ricercare le aule
Priorità	3
Versione	1.0
Categoria	Linguaggio
Sotto Requisiti
001	Dovrà avere la possibilità di avere un filtro per la ricerca (docente, aula o  classe)
002	La funzione dovrà tenere conto della posizione corrente dell’utente
003	La funzione dovrà mostrare a schermo o indicativamente il percorso da svolgere per arrivare alla destinazione
004	La funzione dovrà funzionare tramite il gps integrato del dispositivo senza dover installare niente di esterno.

2.3	   Use case

 




 

2.4	   Pianificazione

 
 
2.5	   Analisi dei mezzi

2.5.1	Software

Per la realizzazione del progetto abbiamo utilizzato le seguenti librerie:
AR.js – 2.2.2	Questa libreria l’abbiamo utilizzata per la realtà aumentata, precisamente per leggere i codici QR in modo da visualizzare gli orari attraverso degli oggetti virtuali.
Plugin Firefox Selenium IDE – 3.16.1	Questo programma l’abbiamo utilizzato per ricavare i dati dell’orario scolastico attraverso il sito della scuola. Selenium permette di registrare delle interazioni con dei siti web per aiutare a generare e mantenere l’automazione del sito, facendo dei test.

Bootstrap - 4.4.1	Questa strumento è stato utilizzato per tutto quello che concerne la parte grafica del nostro sito web, dando a disposizione degli strumenti veramente performanti e puliti con un’ottima documentazione intuitiva.
Selenium webdriver - 3.141.59	Permette di definire quale driver browser dovrà essere utilizzato per eseguire i test e le varie operazioni sul sito in modo automatizzato. Il web browser che utilizziamo è Chrome.
BeautifulSoup – 4.4.0	Permette di ricavare i dati dal sito. Precisamente è un “parser” di linguaggi xml e html.
Flask – 1.1.1	È un micro web framework.
Re	Libreria per le espressioni regolari
Time	Libreria che contiene dei metodi per il tempo.
Datetime	Libreria che contiene dei metodi per le date.
Selenium	Package di selenium che contiene diverse librerie.
Beautiful soup	Libreria che permette di parsare del codice HTML.


	
2.5.2	Hardware

Visto che il nostro progetto è interamente lato web, non abbiamo dovuto utilizzare delle macchine particolari per lo sviluppo. Abbiamo utilizzato semplicemente i nostri laptop (Windows, Linux, Mac).





3.	Progettazione e Implementazione

3.1	   Location

L’utente entrerà dalla porta di entrata della scuola. All’inizio del quarto piano sarà presente un codice QR per entrare nel nostro sito web. Nel menu principale del nostro sito ci sarà una breve guida utente per guidarlo nell’utilizzo dell’applicativo. Una volta capito il funzionamento potrà scegliere quale funzione utilizzare.

3.2	   Pattern

Il codice QR è il marchio di fabbrica di un tipo di codice a barre a matrice (o codice a barre bidimensionale). Un codice a barre è un'etichetta ottica leggibile dalla macchina che contiene informazioni sull'elemento a cui è allegato. In pratica, un codice QR spesso contiene dati per un localizzatore, identificatore o tracker che puntano a un sito Web o un'applicazione. Un codice QR è costituito da quadrati neri disposti su una griglia quadrata su uno sfondo bianco, che possono essere letti da un dispositivo di imaging come una fotocamera ed elaborati utilizzando la correzione dell'errore Reed-Solomon fino a quando l'immagine non può essere interpretata in modo appropriato. I dati richiesti vengono quindi estratti dai motivi presenti in entrambi i componenti orizzontali e verticali dell'immagine.
 Tutti i codici QR hanno una forma quadrata e includono tre contorni quadrati negli angoli in basso a sinistra, in alto a sinistra e in alto a destra. Questi contorni quadrati definiscono l'orientamento del codice. I punti all'interno del codice QR contengono informazioni sul formato e sulla versione, nonché il contenuto stesso. I codici QR includono anche un certo livello di correzione degli errori, definito come L, M, Q o H. Una bassa quantità di correzione degli errori (L) consente al codice QR di contenere più contenuti, mentre una maggiore correzione degli errori (H) rende il codice più facile da scansionare. I codici QR hanno due vantaggi significativi rispetto agli UPC tradizionali: i codici a barre comunemente utilizzati negli imballaggi al dettaglio. Innanzitutto, poiché i codici QR sono bidimensionali, possono contenere significativamente più dati di un UPC monodimensionale. Mentre un UPC può includere fino a 25 caratteri diversi, un codice QR 33x33 (versione 4), può contenere 640 bit o 114 caratteri alfanumerici. Un codice QR 177x177 (versione 40) può contenere fino a 23.648 bit o 4.296 caratteri. Un altro vantaggio dei codici QR è che possono essere scansionati da uno schermo. 
3.2.1	Come creare un QR Code

Per creare un codice QR non è difficile. Non lo creeremo manualmente ma utilizzeremo strumenti disponibili su Internet. Il sito Web per la creazione del codice QR scelto da noi è qr-code-monkey.com. Un semplice sito Web che consente di creare codici QR modificandone lo stile per renderlo più bello esteticamente.
3.2.2	Come creare un Pattern

Per creare un pattern abbiamo utilizzato il seguente sito web: 
https://au.gmented.com/app/marker/marker.php

Una volta entrati per generare un pattern corretto basta inserire le seguenti impostazioni e una volta fatto sarà possibile salvarlo.

 




3.2.3	QR Code Floor

Noi avremo un QR Code all’inizio del quarto piano che porterà direttamente al nostro sito simile al seguente:






3.3	   Database

 




3.4	   Creazione del database

3.4.1	Introduzione

Come prima cosa, bisogna ovviamente creare il database School_Hours per riuscire ad inserire tutti gli orari dell’anno scolastico. Per farlo è molto semplice.

3.4.2	Codice





3.4.3	Entità Classroom

3.4.3.1	Introduzione 
Questa entità ha il compito di racchiudere tutte le classi del quarto piano attraverso il nome dell’aula e il codice. Successivamente questa entità verrà poi collegata a School_Hour per assegnare all’aula corrispondente il proprio orario scolastico.
3.4.3.2	Progettazione
 
Attributi
Code:	Codice univoco che rappresenta e distingue ogni aula dalle altre.
Name:	Nome dell’aula in questione.

3.4.3.3	Codice
 
3.4.4	Entità School_Hour

3.4.4.1	Introduzione 
Questa entità ha il compito di racchiudere tutti gli orari del quarto piano attraverso vari parametri. Successivamente questa entità assegnerà alla entità Classroom l’orario corrispondente.
3.4.4.2	Progettazione

Attributi
Id:	Id univoco per identificare l’orario scolastico.
Start_time:	Orario di inizio della lezione in questione.
End_time:	Orario di fine della lezione in questione.
Teacher:	Docente assegnato.
Day:	Giorno della lezione.
School_subject:	Materia scolastica.

3.4.4.3	Codice
 

3.5	Selenium
Selenium è un Framework di test sviluppato in Java che permette di interagire con diversi browser Web. In effetti permette di realizzare dei test dinamici che facilitano dei test funzionali e quindi non richiedono l’esecuzione di un software. Per realizzare i nostri test abbiamo utilizzato l’estensione che si chiama Selenium IDE che può essere installata su qualsiasi browser. 

3.5.1	Estrapolazione dati (Scraper)
Per estrapolare i dati dal sito abbiamo creato uno script chiamato Scraper. Questo è uno script molto potente che permette in generale di estrapolare qualsiasi dato desiderato da qualsiasi sito possibile immaginabile. Per realizzarlo ci siamo basati su un esempio fornito dal nostro professore, però modificandone alcune parti.
3.5.2	Assegnazione del browser Firefox
Il browser che abbiamo utilizzato per effettuare i vari test è Mozilla Firefox, quindi nello script abbiamo dovuto specificare quale driver utilizzare. Per farlo abbiamo solo dovuto scrivere la seguente riga di codice:
 

3.5.3	Mascheramento del browser
Ogni volta che avviamo il nostro Scraper questo aprirà il browser Google Chrome, andrà sul sito dell'orario della scuola ed eseguirà i vari test. Per nascondere la finestra del browser e evitare di mostrare all’utente le procedure eseguite dallo Scraper, è possibile mascherare il tutto aggiungendo i seguenti parametri:

Il metodo Options permette di aggiungere delle opzioni aggiuntive al Web driver Selenium. Successivamente l’attributo headless permette di nascondere la finestra del browser. 
3.5.4	Ricerca e recupero dati dell’orario scolastico
Il metodo get_timetable permette di ricercare e recuperare dall’orario scolastico le lezioni di una determinata classe.

Il parametro classroom_name è una stringa che corrisponde al nome della classe.



3.5.5	Aggiunta di un sito web
Per raggiungere un sito web dobbiamo fare una richiesta GET con webdriver di Selenium.

Il parametro self.url corrisponde al URL del orario scolastico. Esso viene passato quando si istanzia la classe Scraper.

3.5.6	Verifica caricamento degli elementi
Questo comando permette di verificare che un determinato elemento sia caricato correttamente. All’interno del metodo loaded_check bisogna mettere l’id dell’elemento che disideriamo caricare. In questo caso l’id corrisponde al link interno “corsi”.

3.5.7	Ricavare elementi HTML
Per potere ricavare un elemento HTML con Selenium bisogna utilizzare il metodo: find_element_by_id che permette di trovare un elemento con un determinato id.
Per cliccare diversi elementi di un sito con Selenium bisogna utilizzare il metodo click.
Ad esempio questa linea di codice permette di cliccare il link interno “corsi”.

3.5.8	Scrittura nome della classe
Per potere scrivere il nome della classe all’interno della barra della ricerca abbiamo utilizzato il seguente codice. Esso permette di selezionare la barra di ricerca e di cercare l’orario di una determinata classe.

3.5.9	Cancellazione barra di ricerca
Il metodo clear permette di cancellare il contenuto presente all’interno della barra di ricerca (ricerche precedenti rimaste nella barra).

3.5.10	Scrittura all’interno della barra 
Il metodo send_keys permette di scrivere all’interno della barra di ricerca.

Il parametro classroom_name corrisponde al nome della classe che si vuole cercare. Questo parametro viene passato dal metodo get_timetable.

3.5.11	Avvio della ricerca
Questa linea di codice permette allo Scraper di eseguire la ricerca attraverso i parametri inseriti nella barra di navigazione del sito degli orari scolastici.


3.5.12	Parsing dei dati
Una volta che abbiamo scelto la classe dovevamo selezionare la tabella dell’orario e iniziare a “parsare” i dati. Per farlo abbiamo aggiunto queste linee di codice dove utilizziamo la libreria beautiful soup.




All’interno del metodo BautifulSoup possiamo aggiungere i seguenti parametri:
page_source	Attributo che permette di acquisire il codice HTML di qualsiasi pagina web.
features	Parametro che definisce quale libreria viene utilizzata per catturare i dati all’interno della pagina web.
html5lib	Libreria per l’analisi del HTML. Utilizziamo questa libreria per catturare i dati all’interno della pagina web.


Con il metodo find possiamo andare a cercare nella pagina web un determinato tag con un determinato id.
Prima di “parsare” i dati bisogna controllare se la tabella cercato contiene dei dati, questo perché potrebbe essere una settimana di vacanza dove non sono presenti lezioni. Inseguito per potere selezionare gli elementi della tabella dobbiamo cercare tutti tag tr che contengono dei tag td o th. Per farlo abbiamo aggiunto la seguente linea di codice.

Con il metodo find_all possiamo catturare un tag che presente più volte all’interno della pagina web. Inseguito abbiamo pensato anche in quale modo salvare le varie informazioni all’interno di un file JSON.
3.5.13	Struttura del nostro JSON

Per creare la seguente struttura abbiamo creato e utilizzato le seguenti variabili.

result	Dizionario che contiene gli orari scolastici di una classe. Al suo interno ci sono i seguenti elementi:
•	is_holiday serve per definire se non ci sono lezioni.
•	timetable contiene i dati dell’orario scolastico. 
day	Dizionario che contiene il giorno in forma testuale e le materie del giorno Al suo interno ci sono i seguenti elementi:
•	day corrisponde alla data del giorno.
•	subjects contiene le materie del giorno.
subjects	Array che contiene le materie del giorno.
lesson	Dizionario che contiene i dati della lezione. Al suo interno ci sono:
•	time corrisponde all’ora della lezione
•	lesson corrisponde al nome della lezione
•	teacher corrisponde al nome dell’insegnante
•	classes corrisponde al nome della classe 

3.5.14	Parte codice importante

Riga 93	Il rimo ciclo corrisponde ad ogni elemento tr della tabella.
Riga 95	Il secondo ciclo corrisponde ad ogni elemento td della tabella.
Riga 97 - 103	La variabile first_time permette al primo ciclo di inserire all’interno del dizionario result all’elemento timetable il giorno della settimana. Per i cicli successivi fino al giorno successivo si deve inserire i dati catturati all’interno del dizionario lesson.
Riga 104-126	Viene inserito per ogni elemento del dizionario lesson i dati dell’orario scolastico.

Alcuni metodi utilizzati per questo codice sono i seguenti:
has_attr	Permette selezionare un tag con un determinato attributo (class, id, style, …)

text.Strip	Permette di selezionare il contenuto di un tag.
append	Permette aggiungere degli elementi ad un array.
parse_classe	Metodo creato da noi per potere formattare nel modo corretto la classe. All’interno di questo codice abbiamo realizzato un’espressione regolare che corrisponde al testo che vogliamo scrivere all’interno del dizionario classe.


3.6	Flask
Flask è un mini-framework in Python che viene utilizzato per lo sviluppo web e permette di creare dei propri siti web in modo dinamico e interattivo.  
Abbiamo creato un file che si chiama app.py che sarà l’applicazione flask. All’interno per definire che si tratta di un flask dobbiamo importare la libreria flask e aggiungere la seguente linea di codice.

Inseguito bisogna definire la app routing che viene utilizzato per mappare l’URL specifico con la funzione associata che intende svolgere alcune attività (struttura simile al MVC).
Nel nostro caso l’URL è associato alla funzione aule che permette di stampare l’orario di una determinata classe. Sì può anche aggiungere come parametro il tipo di richiesta che si vuole fare. In questo caso utilizziamo il metodo GET che consiste nell’accordare all’indirizzo della pagina web i diversi parametri contenenti i dati che si vogliono trasmettere. In questo caso vogliamo trasmettere se mostrare i dati della settimana corrente o quella successiva.
@app.route('/aule', methods=['GET'])
Per ricavare i parametri che sono presenti nel URL bisogna usare il metodo request.args.get.





3.7	Sito Web
Questa sezione è dedicata alla spiegazione del nostro sito web. Il nostro sito web è diviso in due parti:
•	L’interfaccia dedicata all’utente dove potrà utilizzare lo scanner oppure leggere la nostra guida ufficiale.
•	L’interfaccia dedicata agli amministratori del sistema.

3.7.1	Interfaccia admin

3.7.1.1	Accesso alla interfaccia admin
Per accedere alla nostra pagina admin bisogna scrivere nel tab url del browser il seguente indirizzo:
 

3.7.1.2	Spiegazione interfaccia
Una volta entrati apparirà la seguente schermata

 


3.7.1.2.1	Sezione Classrooms
La sezione Classrooms serve per gestire le varie classi.
In questo caso è presente una singola aula (420 (A-417)). Ne noi volessimo aggiungerne altre bisogna semplicemente inserire il nome della classe nel seguente formato:
nome (nome_specifico)
Una volta aggiunto il nome cliccare il bottone Add per aggiungerla.
Dopo aver seguito i seguenti passaggi per ogni aula comparirà un piccolo menu personale che permette di gestire la classe stessa.
 
Delete:	Permette di rimuove l’aula in questione.
Save changes:	Una volta modificato il nome dell’aula permette di salvare le varie modifiche avvenute su essa.
Refresh timetable:	Aggiorna gli orari delle lezioni della settimana attuale.
Refresh all:	Stessa cosa di Refresh timetable ma di tutte le aule presenti nella lista.

3.7.1.2.2	Sezione School hours
La sezione School hours permette di gestire tutti gli orari scolastici di tutte le aule presenti nella lista della sezione Classrooms.
Una volta inserita l’aula desiderata e premuto refresh della pagina dopo circa un secondo usciranno gli orari della settimana della aula desiderata. Nel nostro caso abbiamo scelto l’aula 420 e questo è stato il risultato:
 



3.7.2	Guida utente ufficiale
Nella interfaccia utente è possibile raggiungerla attraverso il seguente link:
 
3.7.2.1	Introduzione
In questa breve guida verrà spiegato in breve come utilizzare la nostra applicazione in modo semplice e veloce.
3.7.2.2	Passaggi

3.7.2.2.1	Passo 1 	
Come prima cosa assicurarsi che siamo sulla homepage del sito ufficiale.
È possibile accedersi nei seguenti modi:
•	Andando sul nostro sito <indirizzo-sito>
•	Tramite il QR Code appeso al quarto piano



3.7.2.2.2	Passo 2
Ora che ci troviamo all'interno del menu bisogna andare in fondo e cliccare Prova ora per testare il QR Code Scanner.
 
3.7.2.2.3	Passo 3
Nel passo tre bisogna semplicemente accettare al browser il permesso di accedere alla vostra webcam del pc/tablet/telefono.
 

3.7.2.2.4	Passo 4
Infine puntando al pattern dell’aula desiderata apparirà un popup con al suo interno l’orario attuale della materia che si sta svolgendo nell’aula in quel momento.

3.7.2.2.5	       Passo 5 (facoltativo)


3.8	Installazione server
Questa parte si occupa di installare il server e tutto il necessario per far funzionare l’applicazione. 
3.8.1	Requisiti
Come prima cosa bisogna dare un’occhiata ai requisiti e controllare che si hanno tutte le cose elencate sotto:
•	Sistema operativo: Ubuntu o derivate con sistema grafico.
•	Connessione internet stabile.

3.8.2	Come avviare lo script
Per avviare lo script bisogna semplicemente inserire il seguente comando nel terminale:
 

3.8.3	Spiegazione script install_ubuntu.sh
 
La prima parte installa il necessario per far funzionare l’applicazione web. Precisamente installa python3.8 e pip(gestore librerie python). Una volta fatto ciò installa setuptools che si tratta di una libreria base utilizzata dalle altre librerie. Infine installa le librerie necessarie di python.
 
La seconda parte permette di installare il reverse proxy. Una volta completata tutta l’istallazione, il server è pronto per essere utilizzato correttamente.


3.8.4	Spiegazione script uninstall_ubuntu.sh
Questo script permette semplicemente di fare le operazioni inverse di quello precedente ovvero disinstallare il server.
3.9	Struttura generale
Questo capitolo spiega la struttura generale dell’applicazione. La struttura è composta nel seguente modo:
•	Web server: Permette di fornire il sito web agli utenti
•	Reverse proxy: Permette di fornire un accesso sicuro attraverso https.


3.10	Web server 
L’applicazione web è stata sviluppata in python utilizzando il micro web framework Flask. Come web server utilizziamo quello di sviluppo integrato con Flask invece di uno apposito (ad esempio uWSGI), siccome abbiamo avuto problemi a farlo funzionare. Il web server integrato regge un traffico piccolo, ma per ambienti di produzione è meglio usarne uno più performante.




3.10.1	Lista file

•	app.py: Contiene l’inizializzazione dell’applicazione di Flask.
•	bgtasks.py: Contiene dei metodi per eseguire della azioni in background.
•	classroom.db: File del database di SqlLite.
•	db.py: Contiene le definizioni dei modelli del database.
•	flask_config.py: Contiene la configurazione di Flask.
•	geckodriver: Driver che permette all’applicativo Selenium di interagire con il browser.
•	routes.py: Definisce i percorsi URL del sito(controller).
•	run.py: Punto di entrata dell’applicazione web.
•	scraper.py: Estrae gli orari dal sito della scuola.
•	static: 



3.11	Reverse Proxy
Il reverse proxy fornisce una connessione sicura HTTPS con l'applicazione web. Questo è stato necessario perchè AR.js richiede una connessione sicura tra il server e il client. Come software abbiamo usato Nginx. Il file di configurazione di Nginx è situato nella cartella /Proxy/nginx.conf. Nella stessa cartella sono presenti il certificato TLS e la chiave privata necessari all'uso di HTTPS. Nella repository è già presente un certificato di prova (Attenzione! Questo certificato è solo di prova, sostituirlo con uno ufficiale!).
3.12	Struttura dei file



4.	Test dei requisiti







 
















5.	Test
Numero Test	Descrizione	Aspettative	Risultato
1	Inserire correttamente i dati all’interno delle tabelle classroom e school_hour.	Si dovrebbe poter visualizzare i dati inerenti alla lezione attuale.	Funziona

       Codice di test:









