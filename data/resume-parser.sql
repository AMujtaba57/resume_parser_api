--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Ubuntu 14.1-2.pgdg20.04+1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_keyword; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_keyword (
    id bigint NOT NULL,
    keyword_value character varying(100) NOT NULL,
    keyword_tag_id bigint NOT NULL
);


ALTER TABLE public.api_keyword OWNER TO postgres;

--
-- Name: api_keyword_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_keyword_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_keyword_id_seq OWNER TO postgres;

--
-- Name: api_keyword_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_keyword_id_seq OWNED BY public.api_keyword.id;


--
-- Name: api_keywordtag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_keywordtag (
    id bigint NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.api_keywordtag OWNER TO postgres;

--
-- Name: api_keywordtag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_keywordtag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_keywordtag_id_seq OWNER TO postgres;

--
-- Name: api_keywordtag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_keywordtag_id_seq OWNED BY public.api_keywordtag.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: api_keyword id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keyword ALTER COLUMN id SET DEFAULT nextval('public.api_keyword_id_seq'::regclass);


--
-- Name: api_keywordtag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keywordtag ALTER COLUMN id SET DEFAULT nextval('public.api_keywordtag_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: api_keyword; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_keyword (id, keyword_value, keyword_tag_id) FROM stdin;
1	.net	2
2	2checkout	1
3	2d	3
4	3d	3
5	abap	2
6	accord.net	4
7	acrobat	1
8	actionscript	2
9	activision engine	1
10	ada	2
11	adabas	1
12	adminer	1
13	ado.net	1
14	adobe	1
15	agile	3
16	ai	3
17	aix	1
18	ajax	1
19	alchemy	1
20	algol	2
21	alice	2
22	alipay	1
23	altibase	1
24	amazon athena	1
25	amazon emr	1
26	amazon keyspaces	1
27	amazon lumberyard	1
28	amazon machine learning	1
29	amazon pay	1
30	amazon quicksight	1
31	amazon rds	1
32	amazon redshift	1
33	amazon sagemaker	4
34	anaconda	4
35	analysis	3
36	analytics	3
37	analyzer	3
38	analyzing	3
39	android	4
40	android pay	1
41	android studio	1
42	angular	4
43	angular.js	4
44	angularjs	4
45	ansi	2
46	ansible	1
47	ant	1
48	antivirus	1
49	apache	4
50	apache flink	4
51	apache kafka	4
52	apache spark	4
53	apache wicket	4
54	apexsql monitor	1
55	api	2
56	apl	2
57	app watch	4
58	appgamekit	1
59	appium	4
60	apple pay	1
61	applix	1
62	apps	3
63	appstore	1
64	appworx	1
65	ar	1
66	arcgis	4
67	arcgixb	4
68	architecting	3
69	archiving	3
70	arcsight	4
71	arduino	1
72	areva	4
73	arm	1
74	articulate	1
75	ascii	2
76	asl	2
77	asp	4
78	asp.net	4
79	asp.net core	4
80	assembly	2
81	assembly language	2
82	atom	2
83	atom solidity linter	1
84	audacity	1
85	audit	4
86	authorize.net	1
87	autocad	1
88	autofac	4
89	automation	3
90	automl	1
91	autosys	1
92	avionics	1
93	awk	2
94	aws	4
95	aws glue	1
96	aws lake formation	1
97	axure	1
98	azure	4
99	azure cosmos db	1
100	azure synapse analytics	1
101	baas	1
102	backbone.js	4
103	backbonejs	4
104	backdrop cms	1
105	backend	3
106	backtrack	1
107	bbc basic	2
108	bi	1
109	bigml	4
110	bigquery	1
111	bios	1
112	bitbucket	1
113	blender	1
114	blizzard engine	4
115	blockchain	3
116	bluesnap	1
117	bolt	1
118	bookshelf.js	4
119	bookshelfjs	4
120	bootstrap	2
121	bottle	4
122	braintree	1
123	bridging	3
124	buildbox	1
125	c	2
126	c#	2
127	c++	2
128	cabling	3
129	caffe	1
130	cakephp	2
131	card.io	1
132	cd/ci	1
133	celtx	1
134	centos	1
135	cerberus x	1
136	cfr	4
137	cgi	4
138	cgs	4
139	cherrypy	4
140	cisco	1
141	cloud	1
142	cloudera	1
143	cmake	1
144	cmod	1
145	cms	1
146	cmvc	4
147	cobol	2
148	cocoa	4
149	cocos2d	4
150	codeigniter	4
152	coldfusion	1
153	compiler	1
154	compiling	3
155	complexity	3
156	computer vision	3
157	computing	3
158	configuring	3
159	construct 3	2
160	coral	1
161	coredata	4
162	corel	1
163	corona	4
164	cpanel	1
165	crm	1
166	cryengine	4
167	cryptography	1
168	cs5	1
169	css	2
170	cuda	1
171	cuv	4
172	cxml	1
173	cyberark	1
174	cybersecurity	3
175	cygwin	1
176	dapper	4
177	dart	2
178	data science	3
179	data warehouse	4
180	database	3
181	database concepts	3
182	databricks	4
183	datacamp	1
184	dataflex	1
185	datalab	1
186	datarobot	1
187	daz3d	1
188	db	3
189	db visualizer	1
190	db2	1
191	dbflow	1
192	dbms	1
193	dbschema	1
194	ddos	1
196	debian	1
197	debugging	3
198	deep learning	3
199	delphi	2
200	deployment	3
202	designer	3
203	desktop	3
204	devart	1
205	developer	3
206	development	3
207	devops	4
208	dhcp	3
209	dhtml	1
210	digital ocean	4
211	django	4
212	dlib	1
213	dns	3
214	docker	1
215	dockerizing	3
216	docking	3
217	doctrine	4
218	dojo	4
219	dos	1
220	dot-abi-cli	1
221	dotcms	1
222	dotnet	2
223	dreamweaver	1
224	drupal	4
225	dsl	1
226	dudaone	1
227	dwolla	1
228	dynamics	3
229	dynamodb	1
230	e-check	1
231	easy ar	1
232	ec2	1
233	eclipse	1
234	edi	4
235	edifact	1
236	edifecs	1
237	edrms	4
238	eigrp	3
239	elastic search	1
240	elixir	2
241	emass	1
242	embark	4
243	embedded	3
244	emr	4
245	ems	4
246	ems sql manager	1
247	encoding	3
248	encryption	3
249	engineering	3
250	ent	4
251	enterprise	2
252	entity	4
253	entity framework	4
254	entity framework core	4
255	epicor	4
256	epm	1
257	erd	3
258	erlang	2
259	erp	4
260	esm tools	1
261	eth fiddle	4
262	ethereum-abi-ui	4
263	ethereumj	4
264	ethereumjs vm	4
265	etherlime	4
266	ethernet	1
267	ethpm-spec	4
268	etl	1
269	express.js	4
270	extranet	1
271	f#	2
272	farm	4
273	fastapi	4
274	filemaker	1
275	filenet	1
276	finance	1
277	firebase	1
278	firewall	3
279	firmware	1
280	flask	4
281	forth	2
282	fortran	2
283	framework	4
284	frontend	3
285	ftp	3
286	fuelphp	4
287	functional programming	3
288	fusion 2.5	1
289	gamebench	1
290	gamemaker studio 2	1
291	ganache	1
292	ganache cli	1
293	genome	1
294	gensim	4
295	geth	1
296	gideros	4
297	gis	4
298	git	1
299	github	1
300	gitlab	1
301	glueviz	1
302	go	2
303	go ethereum	1
304	gocardless	1
305	godot	1
306	golang	2
307	google bigquery	1
308	google cloud automl	1
309	google cloud bigtable	1
310	google cloud platform	4
311	google cloud spanner	1
312	google colab	1
313	gorm	1
314	graphdbgraphic	1
315	graphviz	1
316	groovy	2
317	gui	1
318	hadoop	4
319	hadoop hdfs	1
320	haproxy	1
321	haskell	2
322	haxe 4	2
323	helix core	1
324	heroku	1
325	hibernate	1
326	houdini fx	1
327	html	2
328	html5	2
329	iaas	3
330	ibm db2	1
331	ibm db2 warehouse	4
332	ibm watson	1
333	icloud	1
334	idl	2
335	iis	1
336	image processing	3
337	imap	3
338	implementation	3
339	incredibuild	1
340	infura	1
341	inpage	1
342	insight	4
343	installation	3
344	integrating	3
345	integration	3
346	interfaces	3
347	internet of things	3
348	intranet	1
349	intune	1
350	invision	1
351	ionic	4
352	ios	1
353	iot	3
354	ip	3
355	ipps	4
356	ipsec	3
357	ipv4	3
358	ipv6	3
359	irs	4
360	isdn	1
361	jamf	1
362	java	2
363	javafx	2
364	javascript	2
366	jdk	1
367	jenkins	1
368	jira	1
369	jit	1
370	joomla	1
371	jquery	2
372	js	2
373	jscript	2
374	json	3
375	json rpc api	1
376	json-rpc	1
377	julia	2
378	jupyter notebook	1
379	keras	4
380	kernel	1
381	knack	1
382	knime	1
383	kobiton	1
384	kotlin	2
385	kubernetes	1
386	l2tp	3
387	lan	3
388	landesk	3
389	laravel	4
390	latex	1
391	ldap	3
392	lift	4
393	linq	4
394	linux	1
396	liquidity	1
397	logic	3
398	logical	3
399	longrange	1
400	lua	2
401	lync	1
402	mac os	1
403	machine learning	3
404	magento	1
405	mahout	1
406	management	3
407	marmalade	1
408	matlab	2
409	maven	1
410	mean	3
411	memsql	1
412	mern	3
413	metamask	1
414	meteor	4
415	mevn	3
416	microsoft access	1
417	microsoft power bi	1
418	microsoft sql server	1
419	microsoft windows	1
420	middleware	1
421	mist	1
422	mixamo	1
423	mlflow	1
424	mlops	3
425	mlpack	1
426	mobile angular ui	4
427	mobincube	1
428	mojolicious	4
429	mongodb	1
430	monogame	4
431	ms access	1
432	ms dos	1
433	ms excel	1
434	ms exchange	1
435	ms sql	1
436	ms windows	1
437	ms word	1
438	ms.net	1
439	msxml	1
440	multitask	3
441	multitasking	3
442	multithread	3
443	multithreading	3
444	mvc	4
445	mvc 4	4
446	mvc 5	4
447	mvp	3
448	mvs	1
449	mvvm	3
450	my sql workbench	1
451	mysql	3
452	nat	3
453	nativescript	4
454	neo4j	1
455	netapp	1
456	netbeans	1
457	netcdf	3
458	nethereum	4
459	netiq	3
460	netsuite	1
461	netware	1
462	network	3
463	network programming	3
464	networking	3
465	next.js	4
466	nginx	1
467	nlp	3
468	nmap	1
469	node	3
470	node.js	4
471	nodejs	4
472	nosql	3
473	ntservers	1
474	numba	4
475	nxt-g	1
476	oauth	1
477	objection.js	1
478	objectionjs	1
479	objective-c	2
480	objectivesql	4
481	odoo	3
482	office	1
483	office365	1
484	oim	1
485	olap	1
486	oltp	3
487	omb	1
488	oms	1
489	onsen ui	4
490	oop	3
491	open nn	4
492	openam	4
493	opencl	4
494	opencv	3
495	opengl	1
497	oracle	4
498	oracle autonomous warehouse	1
499	oracle rdbms	1
500	oracle7	3
501	oracle8	3
502	oracle8i	3
503	oracle9	3
504	oracle9i	3
505	oraclexml	1
506	orange3	1
507	orient db	1
508	orm	3
509	os	3
510	osi	3
511	paas	3
512	parity	3
513	pascal	2
514	payjunction	1
515	paymotion	1
516	payoneer	1
517	paypal	1
518	paysimple	1
519	paytm	1
520	perl	2
521	phaser	1
522	photoshop	1
523	php	2
524	phpcms	3
525	phpmyadmin	1
526	pl/sql	1
527	pop3	3
528	populus	1
529	postgres	3
530	postgresql	3
531	postgressql	3
532	postman	1
533	postscript	2
534	powerbi	1
535	powershell	1
536	ppoe	3
537	prediction	3
538	prolog	2
539	prototype	3
540	prototyping	3
541	prysm	1
542	pure data	3
543	pusher	1
544	putty	1
545	pycharm	1
546	pyethereum	4
547	pygame	4
548	pylons	4
549	pyqt	1
550	pyspark	4
551	python	2
552	pytorch	4
553	qa	3
554	qlik	1
555	qos	3
556	qtp	3
557	quality assurance	3
558	quixel bridge	1
559	r	2
560	r&d	3
561	rabbitmq	1
562	raspberry pi	1
563	ravendb	3
564	rdbms	3
565	rdlc	3
566	react	4
567	react native	4
568	react.js	4
569	reactjs	4
570	reconfiguration	3
571	redhat	3
572	redshift	1
573	redux	4
574	remix ide	1
575	rest	3
576	rest framework	4
577	restapi	4
578	restful	4
579	robomongo	1
580	ror	2
581	rpg maker	1
582	rsa	3
583	rstudio	1
584	rtp	3
585	ruby	2
586	ruby on rails	2
587	rust	2
588	s3	1
589	salesforce	1
590	saml	2
591	sandbox	1
592	sap	1
593	sap data warehouse cloud	1
594	sap sybase ase	1
595	sas	3
596	scala	2
597	scalegrid	1
598	sccm	3
599	scikit-learn	4
600	scipy	4
601	scm	3
602	scom	3
603	scripting	3
604	scrum	3
606	scsi	1
607	scylladb	3
608	sdk	1
609	sdlcs	3
610	selenium	1
611	selenium web driver	1
612	seo	3
613	sequel pro	1
614	sequelize	3
615	server	1
616	servlet	3
617	servlets	3
618	sftp	3
619	sha	3
620	sharepoint	1
621	shell	1
622	shellscript	1
623	shellscripting	3
624	shopify	4
625	siebel	3
626	sila	3
627	silex	3
628	simula	1
629	siprnet	3
630	sitebuilder	1
631	sitecore	1
632	sklearn	4
633	skrill	3
634	sla	3
635	slaframework	4
636	smart contracts	3
637	smtp	3
638	snapmanager	1
639	snowflake	1
640	soapui	1
641	software assessment	3
642	software assessment management	1
643	software development	3
644	software production	3
645	software production management	3
646	software testing	3
647	solar2d	1
648	solaris	2
649	solaris10	1
650	solaris8	1
651	solaris9	1
652	solarwinds	1
653	solc	1
654	solidity	2
655	sop	3
656	sops	3
657	soql	3
658	spacy	1
659	spark	4
660	spatialos	1
661	speedtree	1
662	spreedly	1
663	springboot	4
664	spritkit	1
665	spss	3
666	spyder	1
667	sqa	3
668	sql	3
669	sql developer	3
670	sql sentry	1
671	sql server	1
672	sql server management studio	1
673	sql+.net	1
674	sqlalchemy	1
675	sqlite	3
676	sqlyog	1
677	sqr	2
678	squarespace	1
679	srs	3
680	saas	3
681	ssis	3
682	ssl	3
683	ssp	3
684	ssrs	3
685	stackby	1
686	stata	1
687	stencyl	1
688	stlc	3
689	stp	3
690	stripe	1
691	subnetting	3
692	sugar orm	1
693	sunos	1
694	swift	2
695	swiftic	1
696	symantec	1
697	symfony	4
698	synchronization	3
699	tableau	1
700	tableplus	1
701	tcl	2
702	tcp	3
703	tcp/ip	3
704	tcpip	3
705	teamdesk	1
706	tencent engine	4
707	tensorflow	4
708	teradata	1
709	tex	1
710	theano	4
711	titanium	1
712	tk	1
713	tkinter	1
714	toad	1
715	truffle	1
716	tsql	3
717	turbogears	4
718	typescript	2
719	typo3	1
720	ubuntu	1
721	ui	3
722	ui/ux	3
723	uml	3
724	unity	1
725	unix	1
726	unreal engine	4
727	urban airship	1
728	user testing	3
729	ux	3
730	vaadin	1
731	vb	3
732	vb basic .net	2
733	vb.net	2
734	vba	3
735	vbscript	2
736	vdi	3
737	vdm	3
738	verilog	2
739	vhdl	2
740	visio	1
741	visual basic .net	2
742	visualstudio.net	1
743	vlan	3
744	vmd	3
745	vms	1
746	voip	1
747	vpn	1
748	vps	3
749	vue.js	4
750	vuejs	4
751	vuforia	1
752	vyper	2
753	wan	3
754	wap	2
755	wap/wml	2
756	web3	4
757	web3.js	2
758	web3j	1
759	webgui	1
760	webmoney	1
761	websphere	1
762	weebly	1
763	weka	1
764	wepay	1
765	win32	1
766	winjs	1
767	winpython	1
768	wireshark	1
769	wix	1
770	wlan	3
771	wml	2
772	wms	1
773	wordpress	3
774	workflow	3
775	workflows	3
776	worldpay	1
777	wsdl	2
778	x++	2
779	xamarin	1
780	xaml	2
781	xcode	1
782	xhtml	2
783	xml	2
784	xmlrpc	1
785	xsl	2
786	yola	1
787	python developer	3
788	.net developer	3
789	ios developer	3
790	android developer	3
791	django developer	3
792	web developer	3
793	blockchain developer	3
794	game developer	3
795	flutter developer	3
796	mobile application developer	3
797	user acceptance testing	3
798	software testers	3
\.


--
-- Data for Name: api_keywordtag; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_keywordtag (id, name) FROM stdin;
1	tool
2	language
3	skill
4	framework
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add keyword	7	add_keyword
26	Can change keyword	7	change_keyword
27	Can delete keyword	7	delete_keyword
28	Can view keyword	7	view_keyword
29	Can add keyword tag	8	add_keywordtag
30	Can change keyword tag	8	change_keywordtag
31	Can delete keyword tag	8	delete_keywordtag
32	Can view keyword tag	8	view_keywordtag
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	api	keyword
8	api	keywordtag
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-02-28 12:43:17.355199+05
2	auth	0001_initial	2022-02-28 12:43:17.485179+05
3	admin	0001_initial	2022-02-28 12:43:17.521882+05
4	admin	0002_logentry_remove_auto_add	2022-02-28 12:43:17.531327+05
5	admin	0003_logentry_add_action_flag_choices	2022-02-28 12:43:17.541683+05
6	api	0001_initial	2022-02-28 12:43:17.56502+05
7	api	0002_rename_netag_keyword_keyword_tag_and_more	2022-02-28 12:43:17.57245+05
8	api	0003_configuration_keywordtag_alter_keyword_keyword_value_and_more	2022-02-28 12:43:17.637589+05
9	api	0004_delete_configuration	2022-02-28 12:43:17.642713+05
10	contenttypes	0002_remove_content_type_name	2022-02-28 12:43:17.661314+05
11	auth	0002_alter_permission_name_max_length	2022-02-28 12:43:17.670755+05
12	auth	0003_alter_user_email_max_length	2022-02-28 12:43:17.680142+05
13	auth	0004_alter_user_username_opts	2022-02-28 12:43:17.68913+05
14	auth	0005_alter_user_last_login_null	2022-02-28 12:43:17.69859+05
15	auth	0006_require_contenttypes_0002	2022-02-28 12:43:17.702568+05
16	auth	0007_alter_validators_add_error_messages	2022-02-28 12:43:17.712007+05
17	auth	0008_alter_user_username_max_length	2022-02-28 12:43:17.727834+05
18	auth	0009_alter_user_last_name_max_length	2022-02-28 12:43:17.738998+05
19	auth	0010_alter_group_name_max_length	2022-02-28 12:43:17.749309+05
20	auth	0011_update_proxy_permissions	2022-02-28 12:43:17.759518+05
21	auth	0012_alter_user_first_name_max_length	2022-02-28 12:43:17.769036+05
22	sessions	0001_initial	2022-02-28 12:43:17.798326+05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: api_keyword_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_keyword_id_seq', 798, true);


--
-- Name: api_keywordtag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_keywordtag_id_seq', 4, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: api_keyword api_keyword_keyword_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keyword
    ADD CONSTRAINT api_keyword_keyword_key UNIQUE (keyword_value);


--
-- Name: api_keyword api_keyword_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keyword
    ADD CONSTRAINT api_keyword_pkey PRIMARY KEY (id);


--
-- Name: api_keywordtag api_keywordtag_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keywordtag
    ADD CONSTRAINT api_keywordtag_name_key UNIQUE (name);


--
-- Name: api_keywordtag api_keywordtag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keywordtag
    ADD CONSTRAINT api_keywordtag_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: api_keyword_keyword_0650340b_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_keyword_keyword_0650340b_like ON public.api_keyword USING btree (keyword_value varchar_pattern_ops);


--
-- Name: api_keyword_keyword_tag_id_63b25fd5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_keyword_keyword_tag_id_63b25fd5 ON public.api_keyword USING btree (keyword_tag_id);


--
-- Name: api_keywordtag_name_d3d857ee_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_keywordtag_name_d3d857ee_like ON public.api_keywordtag USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: api_keyword api_keyword_keyword_tag_id_63b25fd5_fk_api_keywordtag_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_keyword
    ADD CONSTRAINT api_keyword_keyword_tag_id_63b25fd5_fk_api_keywordtag_id FOREIGN KEY (keyword_tag_id) REFERENCES public.api_keywordtag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

