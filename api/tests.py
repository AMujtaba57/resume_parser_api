import json

import requests
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Keyword, KeywordTag


class CreateTaskTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = {
            "name": "test",
        }

    def test_create_task(self):
        """
        :Message: creation of task
        :return: None
        """

        url = "/api/keyword-tag/create/"

        response = self.client.post(path=url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateInvalidTaskTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = {"name": "test"}

    def test_create_task(self):
        """
        :Message: creation of task
        :return: None
        """

        url = "/api/keyword-tag/create/"

        response = self.client.post(path=url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class KeywordTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = {
            "name": "test",
        }

        self.data = KeywordTag(name="test name")
        self.data.save()

    def test_get_specific_keyword(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keyword-tag/retrieve/{self.data.id}/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteKeywordTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = {
            "name": "test",
        }

        self.data = KeywordTag(name="test name")
        self.data.save()

    def test_delete_task(self) -> None:
        """
        Test Delete Task API
        :return: None
        """
        url = f"/api/keyword-tag/delete/{self.data.id}/"
        get_response = self.client.delete(path=url)
        self.assertEqual(get_response.status_code, status.HTTP_204_NO_CONTENT)


class UpdateKeywordTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = KeywordTag(name="test")
        self.data.save()
        self.d = {"name": "test updated"}

    def test_update_keyword(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keyword-tag/update/{self.data.pk}/"
        response = self.client.put(path=url, data=self.d)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_keywords(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = "/api/keyword-tags/list/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateKeywordInvalidTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.data = KeywordTag(name="test")
        self.data.save()
        self.d = {"name": "test updated"}

    def test_update_keyword(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keyword-tag/update/{self.data.pk}/"
        response = self.client.put(path=url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class KeywordManagementTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        keyword_tag = KeywordTag(name="test s df")
        keyword_tag.save()

        self.data = {"keyword_value": "test value", "keyword_tag": keyword_tag.id}
        # self.data.save()

    def test_create_task(self):
        """
        :Message: creation of task
        :return: None
        """

        url = "/api/keywords-management/"

        response = self.client.post(path=url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetTaskTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()

        self.data = {"keyword_value": "test value", "keyword_tag": self.keyword_tag.id}

    def test_get_keyword_tag_list(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = "/api/keywords-management/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTaskTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.headers = {"Content-type": "application/json", "Authorization": "6251655368566D597133743677397A24"}

        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()
        self.data = {"keyword_value": "test value", "keyword_tag": self.keyword_tag.pk}

    def test_put_keyword_tag(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keywords-management/{self.keyword.pk}/"
        response = self.client.put(path=url, data=self.data, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateInvalidTaskTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.headers = {"Content-type": "application/json", "Authorization": "6251655368566D597133743677397A24"}

        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()
        self.data = {"keyword_value": 5, "keyword_tag": self.keyword_tag.pk}

    def test_put_keyword_tag(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keywords-management/{self.keyword.pk}/"
        response = self.client.put(path=url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteTaskTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.headers = {"accept": "application/json", "Authorization": "6251655368566D597133743677397A24"}
        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()
        self.data = {"keyword_value": "test value", "keyword_tag": self.keyword_tag.pk}

    def test_delete_keyword_tag(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keywords-management/{self.keyword.pk}/"

        get_response = self.client.delete(path=url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)


class DeleteNotExistRecordTaskTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.headers = {"accept": "application/json", "Authorization": "6251655368566D597133743677397A24"}
        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()

    def test_delete_keyword_tag(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keywords-management/{self.keyword}9/"

        get_response = self.client.delete(path=url, **self.headers)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


class CreateParserTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """

        super().setUp()

        self.headers = {"Content-type": "application/json", "Authorization": "6251655368566D597133743677397A24"}
        self.data = {
            "firstName": "Amjada",
            "lastName": "Nagrah",
            "jobTitle": "Technical Program Manager/Program Manager",
            "summary": "Amjad has an experience in the domain of Software/IT, particularly in Software Engineer. The "
            "candidate has a total experience of 18 Years and is currently working as Technical Program "
            "Manager/Program Manager at ZDAAS LLC for the last 6.11 years. ",
            "certifications": [],
            "educations": [
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Maharishi University of Management",
                    "location": "Fairfield",
                    "sortOrder": 1,
                },
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Punjab Institute of Computer Sciences",
                    "location": "Lahore",
                    "sortOrder": 2,
                },
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Punjab Institute of Computer Sciences",
                    "location": "Lahore",
                    "sortOrder": 3,
                },
            ],
            "experiences": [
                {
                    "jobTitle": "Technical Program Manager/Program Manager",
                    "startDate": "12/01/2015",
                    "endDate": "16/11/2021",
                    "description": "Baltimore, MD \n Project : Zbizlink \n Project Description : ZBizlink https : "
                    "www.zbizlink.com \n This SaaS-based solution contains approximately 16 "
                    "sub-projects and two web interfacing portals for end users. It is a fully "
                    "integrated solution using a Microsoft SharePoint Portal online for its document "
                    "repository and Microsoft Dynamics CRM 2016 for candidates tracking. It has a "
                    "normalized transactional database and a separate data warehouse for reporting, "
                    "analysis, and statistics. This solution contains high level features such as : \n "
                    "Vendors Management-Manage vendors' data and vendors' performance \n Procurement "
                    "Management-Locates and displays new proposal's RFP/RFR/RFQ etc. and "
                    "evaluates/scores vendors' proposal'submissions. \n Capture Management-Builds "
                    "proposal response templates and plugs in appropriate content, identifies proposal "
                    "team members, and enables collaboration among teams in order to submit successful "
                    "proposal responses. \n Dashboard and Reports-Provides various widgets that "
                    "provide information and drive dynamic collaboration, such as customized matrix "
                    "reports. \n Completed this project within a very tight timeline and budget. "
                    "Coordinated with team of 12 resources on a daily basis to ensure that all work "
                    "performed met expected results. It is quite an accomplishment for a team this "
                    "size, in this timeframe and with this budget to deliver a working software "
                    "product of this size and complexity. The application is getting very high marks "
                    "from business users. \n Other projects include data warehouses, portals, "
                    "architecture and development, conversion, configuration management, "
                    "change management, release management, and testing efforts. \n General "
                    "Responsibilities for all ZDAAS Projects \n Design and direct development of IT "
                    "strategy that supports company's strategic mission and business plan. Implement "
                    "and manage strategy across IT domain. \n Develop and ensure compliance to "
                    "corporate IT standards and policies to ensure compatibility and integration "
                    "throughout company. \n Configure, Install and manage Cloud environments 12 VM "
                    "Servers and three separate regions on Windows Azure for Zbizlink Production and "
                    "Test environments. Prepare always On and Azure Cloud as well as prepared backup "
                    "policies for VM backup, application backup, databases backups and environments "
                    "configurations backup. \n Developed Agile SCRUM artifacts including guidelines, "
                    "standards, and best practices to manage the development of ZBizlink. Oversees "
                    "adherence to, and use of development methodologies, frameworks, and project "
                    "tools. Supports and advises team on all technical and performance-impacting "
                    "issues. \n Strategically plan and manage initiatives consisting of program "
                    "components that meet stakeholder expectations. \n Report to Sr. Executive "
                    "Management; authorize and manage internal and external relationships and "
                    "dependencies across initiative components to ensure successful delivery of the "
                    "program. \n Ensure efficient distribution of the technical and business "
                    "resources; and will coordinate with business executives the initiation or "
                    "continuation of project based on business requirements, business performance and "
                    "available organizational resources. \n Responsible for establishing and executing "
                    "adequate project management controls based on industry accepted methodologies and "
                    "standards. \n Committed to monitor and control cost, schedule, performance and "
                    "risk; to ensure quality and security; overall integration and issues resolution "
                    "and to perform administrative functions. \n Co-ordinate with executive "
                    "management, prepare annual budget and spending strategies, and monitor business "
                    "and financial performance of initiative components from strategic perspective. \n "
                    "Attend and/or leads technical discussions/JAD sessions with application "
                    "designers, developer's, architects, business analysts, senior-level business "
                    "executives, and content strategists to develop complex designs, "
                    "business solutions, and management plans mapped to business demands. \n Manage "
                    "multiple projects and all project requirements-conduct functional and "
                    "non-functional requirements analysis; provides complex project and system "
                    "analysis. \n Manage day to day business tasks and client-driven assignments and "
                    "deliverables using PMI, PMBOK, and Agile development models including SCRUM . \n "
                    "Attend meetings; create and deliver status and project reports to client's and "
                    "their senior technical staff members; facilitates communication between all key "
                    "IT groups, business, and the customer community. \n Recruit and interview "
                    "resources; direct, train, and mentor all individuals and teams. Provides "
                    "governance and oversight. Manage multiple teams simultaneously. Verify and "
                    "validate work quality, timeliness and Agile compliance by resources. \n "
                    "Responsible for all design and development, including : \n Architecture - "
                    "Co-ordinate Microsoft Dynamics CRM architectural, integration parameters with "
                    "internal and external components including interfaces for Zbizlink with "
                    "SharePoint and CRM Dynamics. \n Enhancements, new features and upgrades "
                    "development, testing, deployment, maintenance \n QA/QC, validation and testing "
                    "including UAT \n Production support and maintenance of ongoing operations \n "
                    "Tools & Technology \n Microsoft Office, Microsoft Project, Microsoft Team "
                    "Foundation Server, Microsoft Dynamics CRM 2016 SharePoint 2016 Live, Vision, "
                    "Microsoft Framework 6.0, C#, Java, AngularJS, MVC 5.0, Entity Framework 5.0, "
                    "ASP.NET, SQL Server 2014.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 1,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "18/11/2013",
                    "endDate": "15/07/2015",
                    "description": "Project : Maryland Educators Information System EIS/MSDE \n Budget : $678, "
                    "450 \n Worked in collaboration with MSDE consultants and business users to "
                    "determine the gaps in requirements. Determined functionalities and defined "
                    "workable solutions to bridge gaps, designing the optimum technical solution in "
                    "the context of the client's environment, requirements, and financial resources. "
                    "Ensured the delivery of a quality system design which meets system performance "
                    "requirements, an effective human-machine interface, optimal operational cost, "
                    "and flexibility for future change. \n Responsibilities \n Defined the logical, "
                    "technical, and physical architecture for SharePoint as application platform that "
                    "are consistent with architecture principles, standards, methodologies, "
                    "and best practices. \n Implemented processes automation by creating Custom "
                    "Workflows Activities. \n Customizing Entity, Ribbon, Sitemap, Charts and "
                    "Dashboard in Dynamics CRM 2015. \n Created Custom scripts to migrate Dynamics CRM "
                    "4.0 to Dynamics CRM 2015. \n Analyzed architectural differences between different "
                    "solution methods and the challenges and approaches to integrating solutions built "
                    "on different platforms. \n Migrated 1.2 million Documents using Power Shell from "
                    "file system into SharePoint 2013. \n Created Workflows using Visual Studio 2013 "
                    "and SharePoint Designer 2013 for implementing different business rules. \n "
                    "Created Custom events for business data validation and SharePoint 2013 timer jobs "
                    "for scheduling events using Visual Studio 2013. \n Developed custom web parts to "
                    "update and retrieve Dynamics CRM 2015 entities data. \n Used Scribe Insight for "
                    "Dynamics CRM 4.0 data migration \n Designed and developed application framework "
                    "using ASP.Net, MVC5, MVVM, Entity, LinQ, HTML5, JavaScript and CSS3. \n Optimized "
                    "the Performance of the SharePoint 2013 server by configuring BranchCache and "
                    "creating indexing. \n Automated backup and restore processes for SharePoint "
                    "Content Databases by creating custom PowerShell Scripts. \n Implemented Single "
                    "sign on by implementing ADFS Active Directory Federation Services . \n Created "
                    "queues and relays using Azure Service Bus. \n Conducted interoperability with "
                    "on-premises line of business applications using WCF web services. \n Develop "
                    "custom web parts and integrating enterprise content with SharePoint to include "
                    "developing data repositories, content indexing and workflow. \n Tools & "
                    "Technology : JavaScript, .NET, ADX Studio, Scribe, Microsoft SharePoint 2013, "
                    "Visual Studio 2012, Microsoft Dynamics CRM 2015 and SQL Server 2012.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 2,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "10/10/2012",
                    "endDate": "18/11/2015",
                    "description": "Project : Maryland Accountability and Reporting System MARS \n Budget : $1.8 "
                    "Million and $12.24 Million \n Provided Project Management support to two vital "
                    "software application initiatives supporting the Maryland State Board of Education "
                    ": \n Maryland Accountability and Reporting System MARS which is used for State "
                    "agency users to manage the participating programs, payments, "
                    "and registrations/renewals. \n MARS Portal which is used Statewide for public "
                    "users agencies to participate in different foods/nutrition programs for school "
                    "system. This application developed in Microsoft Framework 2.0 but enhanced to "
                    "Framework 4.0 with C# language at backend. \n Responsibilities \n High "
                    "collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Offered great level "
                    "of collaboration with the finance department and various functional managers to "
                    "ensure IT operational budgets are properly estimated and controlled; provide "
                    "overall financial recommendations, and develop controls and measurements to "
                    "monitor progress. \n Developed, analyze and report IT resource requirements to "
                    "support objectives e.g., staffing, costs needed to meet objectives via resource "
                    "modeling efforts. Participates in and often may lead vendor management efforts "
                    "pertaining to sourcing. \n Facilitated communication between all key IT groups "
                    "and the customer community via participation in meetings and the creation of "
                    "status reporting mechanisms weekly, monthly, and quarterly . \n Supported the "
                    "Senior Technical Staff Members with regard to large scale initiatives through "
                    "resource modeling and providing complex analysis and reporting to Senior IT "
                    "management. \n Performed the code review, and measured the quality matrixes. \n "
                    "Monitored and controlled production supports, enhancements, QA/QC to ensure the "
                    "24/7 availability of applications. \n Coordinated with MSDE stakeholders to "
                    "conduct production support, UAT and ongoing operations. \n Prepared and delivered "
                    "weekly and monthly status reports, budget reports and performance reports. \n "
                    "Tools & Technology \n Microsoft Framework 4.0, C#, AngularJS, MVC 4.0, "
                    "Entity Framework 5.0, ASP.NET, SQL Server 2005.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 3,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "10/10/2012",
                    "endDate": "18/11/2015",
                    "description": "Project : Maryland Accountability and Reporting System MARS \n Budget : $1.8 "
                    "Million and $12.24 Million \n Provided Project Management support to two vital "
                    "software application initiatives supporting the Maryland State Board of Education "
                    ": \n Maryland Accountability and Reporting System MARS which is used for State "
                    "agency users to manage the participating programs, payments, "
                    "and registrations/renewals. \n MARS Portal which is used Statewide for public "
                    "users agencies to participate in different foods/nutrition programs for school "
                    "system. This application developed in Microsoft Framework 2.0 but enhanced to "
                    "Framework 4.0 with C# language at backend. \n Responsibilities \n High "
                    "collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Offered great level "
                    "of collaboration with the finance department and various functional managers to "
                    "ensure IT operational budgets are properly estimated and controlled; provide "
                    "overall financial recommendations, and develop controls and measurements to "
                    "monitor progress. \n Developed, analyze and report IT resource requirements to "
                    "support objectives e.g., staffing, costs needed to meet objectives via resource "
                    "modeling efforts. Participates in and often may lead vendor management efforts "
                    "pertaining to sourcing. \n Facilitated communication between all key IT groups "
                    "and the customer community via participation in meetings and the creation of "
                    "status reporting mechanisms weekly, monthly, and quarterly . \n Supported the "
                    "Senior Technical Staff Members with regard to large scale initiatives through "
                    "resource modeling and providing complex analysis and reporting to Senior IT "
                    "management. \n Performed the code review, and measured the quality matrixes. \n "
                    "Monitored and controlled production supports, enhancements, QA/QC to ensure the "
                    "24/7 availability of applications. \n Coordinated with MSDE stakeholders to "
                    "conduct production support, UAT and ongoing operations. \n Prepared and delivered "
                    "weekly and monthly status reports, budget reports and performance reports. \n "
                    "Tools & Technology \n Microsoft Framework 4.0, C#, AngularJS, MVC 4.0, "
                    "Entity Framework 5.0, ASP.NET, SQL Server 2005.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 4,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "04/10/2012",
                    "endDate": "30/08/2012",
                    "description": "Project : Needles Case Management System \n Budget : $278, 000 \n Director of "
                    "Software Engineering and Project Manager of the Needles Case Management System "
                    "project, a Power Builder application with some of the modules developed by using "
                    "VB Scripts. \n Responsibilities \n Prepared and submitted the Proposal, "
                    "demonstrated the Oral presentation to the client in order to win this contract. "
                    "\n High collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Managed the project "
                    "deliverables by using Agile and SPRINT development model, managed the day to day "
                    "assignments, and verified of work done by resources. \n Managed daily SCRUM "
                    "meetings and biweekly SPRINT meetings. \n Performed the code review, and measured "
                    "the quality matrixes. \n Made sure that team members successfully customized the "
                    "DevExpress and XtraReports library to intergrade Needles report objects to "
                    "provide complete solution for on-demand reports building. \n Achieved a complete "
                    "solution without requiring any design or specifications documents. \n \n Tools & "
                    "Technology \n Microsoft Framework 4.5, C#, Windows Presentation Foundation, Java, "
                    "DevExpress, XtraReports, NHibernate, Sybase, Windows Forms and TeamCity and "
                    "Microsoft Dynamics CRM 2011{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 5,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "01/09/2010",
                    "endDate": "30/09/2014",
                    "description": "Project : Subcabinet for Children Youth & Families Information System SCYFIS Web "
                    "Application Upgrade \n Budget : $2.2 Million \n Team Lead and Solutions Architect "
                    "of the SCYFIS Web Application Upgrade project on behalf of the State of "
                    "Maryland's Governor's Office for Children GOC . Served as the senior solutions "
                    "architect and involved in the development and successful implementation of the "
                    "upgrade. \n The SCYFIS web application was developed in 2003 to help Maryland "
                    "keep track of interagency services provided to children and their families. "
                    "SCYFIS primary users are case worker's, hospital worker's, State agencies, "
                    "service providers, and the general public. \n This initiative convenes the State "
                    "agencies, local partners, and community stakeholders to develop policies and "
                    "initiatives which reflect the priorities of the Governor and the Children's "
                    "Cabinet and resulting in improved services for Maryland's children and youth. \n "
                    "Responsibilities \n to upgrade the classic 'asp SCYFIS web application to .NET "
                    "platform I was involved to achieve the following : \n High collaboration with IT "
                    "management and IT colleagues to translate corporate/functional business and "
                    "information objectives into an IT strategic/tactical business plan and systems "
                    "development. \n Managed the project deliverables by following industry best "
                    "practices and Maryland State defined standards. \n Managed day to day "
                    "assignments, and verification of work done by resources. \n High collaboration "
                    "with business customers in examining solution options and in planning and "
                    "managing multiple IT centric projects. \n Consulted within the IT organization to "
                    "develop appropriate support for IT centric projects from various technology and "
                    "service departments; integrate activities with business units, corporate "
                    "departments, and IT departments to ensure the successful implementation and "
                    "support of project efforts. \n Completed the conversion of Crystal reports XII to "
                    "Crystal Reports 2008 and classic 'asp web application to .NET. \n Tools & "
                    "Technology \n Microsoft Framework 4.5, C#, ASP, MVC 4.0, Entity Framework 4.5, "
                    "SQL Server 2008, Knockout JS, JQuery, HTML 5 and Razor.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 6,
                },
                {
                    "jobTitle": "Technical Lead/IT Director",
                    "startDate": "01/01/2010",
                    "endDate": "18/11/2015",
                    "description": "Project : MDVOTERS II/III \n Director of Software Engineering and technical lead "
                    "started from project transition-in phase to ongoing maintenance and production. "
                    "\n Responsibilities \n Participated in contract transition-in phase and lead the "
                    "effort of the configuration of systems at new environments.\t \n Provided bugs "
                    "fixes and production support services to MDVOTERS II application. \n Provided "
                    "technical supervision to the developer's staff utilized by Canton Group. \n "
                    "Managed the project deliverables by using Agile and SPRINT development model "
                    "managed the day to day assignments, and verified of work done by resources. \n \n "
                    "Tools & Technology \n Microsoft Framework 4.5, VB.NET, Team Foundation Server, "
                    "Oracle 11g, and JIRA.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 7,
                },
                {
                    "jobTitle": "Technical Project Manager/Applications Architect",
                    "startDate": "01/07/2005",
                    "endDate": "31/08/2010",
                    "description": "Project : Managed and Lead more than 20 applications \n Technical Lead and "
                    "Enterprise Architect for a group of primarily .NET applications projects that "
                    "included but are not limited to tracking work activities, adoptions, "
                    "community emergency responses, welfare and social services systems and Maryland "
                    "Secretary's Mail Log. Successfully completed numerous projects, including "
                    "software for a real time interface between the Work Program System WORKS and the "
                    "Client Automated Resource and Eligibility System CARES, SAIL, OHEP, "
                    "Healthy Maryland, MARE, AdoptUsKids and development of reports for various "
                    "applications. \n Responsibilities \n Served as proficient Team Lead more than 20 "
                    "applications, including Cold Fusion, ASP, Delphi, MS Access, and .NET software. "
                    "\n Led at least 17 software professionals, including programmers, testers, "
                    "and technical writers. \n Contributed to and supervised the preparation of the "
                    "contents for Software Development Life Cycle SDLC and design specifications of "
                    "project deliverables. \n Prepared project schedules, project plans, "
                    "resource plans, scope plans, and unit test scripts. Track project schedule and "
                    "variances, activities, defects, issues, and resource assignments. \n Prepared "
                    "weekly and monthly status reports. Prepared and submitted CIO brief documents. \n "
                    "Participated in successful transition of hardware and software to a new Dallas, "
                    "Texas facility. \n Designed the architecture Framework for DHR .NET Applications, "
                    "which is currently used for high volume applications. \n Selected Projects \n "
                    "Work Program System WORKS \n The WORKS application was converted from DataFlex to "
                    ".NET platform. It has both Batch/RTI real time interface with CARES system. WORKS "
                    "serves the Marylander customers by enrolling in FDW/SD activities and tracks "
                    "their hourly attendance, sending auto-generation of Sanction letters to CARES and "
                    "stores Narratives for the customer benefit history. Monthly maintenance job EMR "
                    "to adjust the customer attendance hours as per the defined Federal policies and "
                    "eligibility requirements to maintain/improve the work participation rate. It "
                    "performs case assignments by alphabetical and customized order to the worker's "
                    "and as well as it measures the worker's work performance. \n Single Access "
                    "Interface Links SAIL \n This was the new application developed by using .NET "
                    "platform. It has both Batch/RTI real time interface with CARES system, "
                    "OHEP and Health Maryland System. This application provides single access to "
                    "Marylanders who needed support from Welfare systems by applying into any of "
                    "Maryland State's available Welfare systems. The interfaces with other systems "
                    "were established to transform and streamline the client's applications data. The "
                    "interfaces were developed under the concept of SOA framework and concepts. \n "
                    "Maryland Adoption Resource Exchange MARE System \n This application was converted "
                    "from old classic 'asp/VB Scripts to new .NET platform. This application is used "
                    "by Maryland State caseworker's to manage the child adoptions to and from the "
                    "families. A new interface was established with the U.S central database website "
                    "'AdoptUsKids org' to transfer the cases from Maryland State'system MARE to U.S "
                    "central database. \n Local Transaction Request System LTRS \n This application "
                    "was converted from Delphi to .NET 3.5 and MVC 2.0 platform. It is a critical "
                    "financial application. It used by the local Child Support offices to communicate "
                    "to the State Disbursement Unit SDU, a central office, all requests for financial "
                    "adjustments. It tracks the transaction requests made for local issues concerning "
                    "centrally posted payments. The supervisor processes or denies the requests and "
                    "records comments on the transaction request. It also tracks the age of the "
                    "transaction requests, the contact person, the original date of the request, "
                    "the transaction request type, the TAD representative assigned to the request, "
                    "the request status, and request comments and different reports. \n Local "
                    "Supervisory Surveys Instrument LSRI \n LSRI was revitalized from .NET 1.1 to .NET "
                    "platform and MVC 2.0 Framework. It tracks the employee surveys information and "
                    "provides the ability to edit the survey questions, responses, and response types. "
                    "\n Secretary's Mail Log SML \n SML application was converted from Delphi to .NET "
                    "3.5 and MVC 2.0 platform. This high profile application is used to send/track "
                    "mail notifications across the board. The reports and tasks/assignments serve the "
                    "local offices and employees. \n DHR Framework \n Articulated architectural "
                    "vision, conceptualized and experimented with alternative architectural "
                    "approaches, created models, blueprints, and validated the architecture against "
                    "requirements and assumptions. Studied the organization's goals, needs and given "
                    "the business objectives of the organization and created technology roadmaps, "
                    "made assertions about technology directions and determined their consequences for "
                    "the technical strategy and hence architectural approach. The following areas : "
                    "business units, project services, development, data modeling, database designing, "
                    "and organization's infrastructure were deeply considered during the development "
                    "of the enterprise solution. Designed the architecture and directed the developing "
                    "of .NET Framework for DHR. \n The additional responsibilities for the framework "
                    "development were : \n Created Object Role Model ORM Diagram \n Analysis "
                    "Mechanisms \n Class Responsibility Collaborator CRC Model Class \n Class Diagrams "
                    "\n Participated in development and implementation \n Instructed the technical "
                    "writers to document the how to consume framework during the development of future "
                    "applications \n Led the project with all SDLC responsibilities started from "
                    "analysis to implementation phase \n Tools & Technology \n ASP.NET 2.0, C#, "
                    "SQL Server 2005, Java Script, DHTML, T-SQL & Stored Procedures, Microsoft .NET "
                    "Framework 2.0 and Visual Studio.Net 2005 \n Hospital Billing System \n "
                    "Implemented a Hospital Billing System for Humanim Inc. that allowed users "
                    "including hospital personnel including billing staff, case managers, "
                    "and physicians to submit insurance claims and receive money online. This "
                    "application tracks the submitted claims for the individual customers and "
                    "collected funds. This application complies with HIPPA standards for filling "
                    "charts, and complete codes such HICF 1500, SB92, and CPT to charge insurance "
                    "companies. This application was developed by using Cold Fusion, Java Scripts and "
                    "SQL Server 2000. \n Welcome Maryland Website \n Programmed Welcome MD State "
                    "application for tourism services. It was developed into both ASP and ASP.NET "
                    "platforms. The classic ASP was used to modify the existing site with new design "
                    "and features. ASP.NET/C# was used to provide the feature of content management of "
                    "the site. It provided the flexibility to the administrators for updating/editing "
                    "the contents of complete site.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 8,
                },
                {
                    "jobTitle": "Director of Software Engineering",
                    "startDate": "04/12/2004",
                    "endDate": "18/11/2015",
                    "description": "{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 9,
                },
                {
                    "jobTitle": "Programmer Analyst",
                    "startDate": "01/09/2002",
                    "endDate": "31/01/2004",
                    "description": "Baltimore, MD \n Client : Bermuda Tourism \n Project : Bermuda Tourism In & "
                    "Outbound Call Management \n This application was developed to automate the "
                    "conversion between CSRs Customer Services Representatives and one of the "
                    "multi-nation Company's potential customers through an outbound call process "
                    "system. The code was developed to automate and track outbound telemarketing "
                    "initiatives. The information parsing module was written to review and analyze the "
                    "provided information through inbound calls by the customers/callers and then "
                    "screened the calls which were received with maximum information. An automatic SQL "
                    "scheduled job was developed to send out HTML generated emails to "
                    "callers/customers to make the calls successful. \n Responsibilities \n Developed "
                    "inbound call queue receives calls from customers callers either by telephone or "
                    "by web. \n Developed the outbound call queue to response the calls from inbound "
                    "call queue. \n Wrote the stored procedures to make the inbound call list, "
                    "outbound call list and outbound call queue. \n Wrote stored procedure and SQL Job "
                    "scheduling scripts to send automated dynamic emails to callers. \n Developed the "
                    "ASP pages, form validating scripts. \n Integrated completed website \n Wrote test "
                    "cases, test scripts. \n Performed unit testing, integrating testing. \n \n Tools "
                    "& Technology \n ASP VB Scripts, Visual Basic, SQL Server 2000, Erwin, "
                    "Java Script, HTML/DHTML, Microsoft .NET Framework, T-SQL & Stored Procedures, "
                    "Windows/Web Authentication Solutions, CSS and FrontPage Extensions.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 10,
                },
                {
                    "jobTitle": "Team Leader/Project Coordinator",
                    "startDate": "01/05/2000",
                    "endDate": "30/04/2002",
                    "description": "Baltimore , MD \n Client : Bermuda Tourism \n \n This application was developed "
                    "to automate the conversion between CSRs Customer Services Representatives and one "
                    "of the multi-nation Company's potential customers through an outbound call "
                    "process system. The code was developed to automate and track outbound "
                    "telemarketing initiatives. The information parsing module was written to review "
                    "and analyze the provided information through inbound calls by the "
                    "customers/callers and then screened the calls which were received with maximum "
                    "information. An automatic SQL scheduled job was developed to send out HTML "
                    "generated emails to callers/customers to make the calls successful. \n "
                    "Responsibilities \n Developed inbound call queue receives calls from customers "
                    "callers either by telephone or by web. \n Developed the outbound call queue to "
                    "response the calls from inbound call queue. \n Wrote the stored procedures to "
                    "make the inbound call list , outbound call list and outbound call queue. \n Wrote "
                    "stored procedure and SQL Job scheduling scripts to send automated dynamic emails "
                    "to callers. \n Developed the ASP pages , form validating scripts. \n Integrated "
                    "completed website \n Wrote test cases , test scripts. \n Performed unit testing , "
                    "integrating testing. \n \n Tools & Technology \n ASP VB Scripts , Visual Basic , "
                    "SQL Server 2000 , Erwin , Java Script , HTML/DHTML , Microsoft .NET Framework , "
                    "T-SQL & Stored Procedures , Windows/Web Authentication Solutions , "
                    "CSS and FrontPage Extensions. \n Team Leader/Project Coordinator 05/2000 - "
                    "04/2002 \n M.M. Tech Pvt. Ltd.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 11,
                },
            ],
            "requests": [
                {
                    "type": "Minimum Qualifications",
                    "sortOrder": 0,
                    "queries": [
                        {
                            "sortOrder": 1,
                            "query": "A minimum of six (6) years of experience in User Acceptance Testing.",
                        },
                        {
                            "sortOrder": 2,
                            "query": "A minimum of two (2) years of experience leading teams of software testers.",
                        },
                        {
                            "sortOrder": 3,
                            "query": "A minimum of four (4) years of experience in development of automation scripts "
                            "using Selenium, Selenium Web Driver, QTP, Python or similar tools. ",
                        },
                        {
                            "sortOrder": 4,
                            "query": "A minimum of four (4) years of experience in writing SQL queries with strong "
                            "knowledge of database concepts. ",
                        },
                        {
                            "sortOrder": 5,
                            "query": "A minimum of two (2) years of experience in developing automated scripts for "
                            "RESTful services and integrating them with Jenkins/GIT. ",
                        },
                        {
                            "sortOrder": 6,
                            "query": "A minimum of two (2) years of experience in testing websites across multiple "
                            "browsers, testing web-services, back-end processing and data validation "
                            "utilizing SQL. ",
                        },
                        {
                            "sortOrder": 7,
                            "query": "Strong testing and analytical skills with keen attention to details.",
                        },
                        {"sortOrder": 8, "query": "Experience in Quality Assurance (QA) related functions."},
                        {
                            "sortOrder": 9,
                            "query": "Proven experience working effectively and collaboratively with stakeholders "
                            "from multiple functional teams in an organization. ",
                        },
                    ],
                },
                {
                    "type": "Preferred Qualifications",
                    "sortOrder": 10,
                    "queries": [
                        {
                            "sortOrder": 11,
                            "query": "A minimum of four (4) years of experience as a JAVA/Web application tester on "
                            "complex and dynamic, multi-agency technology projects within the healthcare "
                            "industry. ",
                        },
                        {
                            "sortOrder": 12,
                            "query": "A minimum of four (45) years of experience leading teams of software testers "
                            "performing manual and/or automation testing. ",
                        },
                        {"sortOrder": 13, "query": "Hands-on experience with SQL, HTML, CSS and JavaScript."},
                        {
                            "sortOrder": 14,
                            "query": "Hands-on experience with backend database testing on DB2, SQL, PostgreSQL or "
                            "any other enterprise database systems. ",
                        },
                        {
                            "sortOrder": 15,
                            "query": "Strong technical testing skills using SQL to perform complex DB queries.",
                        },
                        {"sortOrder": 16, "query": "Experience with defect-tracking/management tools such as JIRA."},
                        {
                            "sortOrder": 17,
                            "query": "Experience in testing or supporting State Based Marketplace or healthcare "
                            "systems. ",
                        },
                        {"sortOrder": 18, "query": "Experience with EDI 834 and Medicaid 8001 transactions."},
                        {
                            "sortOrder": 19,
                            "query": "Demonstrated experience with industry standard Quality Assurance best practices "
                            "for Agile and Iterative SDLCs, testing methodologies, version control systems, "
                            "implementation, and deployment activities. ",
                        },
                        {
                            "sortOrder": 20,
                            "query": "Experience in system testing, data warehouse migration testing, data integrity "
                            "testing and data transformation related testing. ",
                        },
                    ],
                },
            ],
        }

    def test_create_parser(self):
        """
        :Message: creation of task
        :return: None
        """
        data = json.dumps(self.data, indent=4)

        url = "http://127.0.0.1:8000/api/parser/"
        response = requests.post(url, data=data, headers=self.headers, auth=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateInvalidParserTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """

        super().setUp()

        self.headers = {"Content-type": "application/json", "Authorization": "6251655368566D597133743677397A24"}
        # data = {}

    def test_create_parser(self):
        """
        :Message: creation of task
        :return: None
        """
        data = json.dumps(self.data, indent=4)

        url = "http://127.0.0.1:8000/api/parser/"
        response = requests.post(url, data=data, headers=self.headers, auth=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateUnauthorizeParserTestCase(APITestCase):
    """test case for creating task api"""

    def setUp(self):
        """
        :return: None
        """

        super().setUp()

        self.headers = {"Content-type": "application/json", "Authorization": "6251655368566D597133743677397A24356"}
        self.data = {
            "firstName": "Amjada",
            "lastName": "Nagrah",
            "jobTitle": "Technical Program Manager/Program Manager",
            "summary": "Amjad has an experience in the domain of Software/IT, particularly in Software Engineer. The "
            "candidate has a total experience of 18 Years and is currently working as Technical Program "
            "Manager/Program Manager at ZDAAS LLC for the last 6.11 years. ",
            "certifications": [],
            "educations": [
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Maharishi University of Management",
                    "location": "Fairfield",
                    "sortOrder": 1,
                },
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Punjab Institute of Computer Sciences",
                    "location": "Lahore",
                    "sortOrder": 2,
                },
                {
                    "degreeName": "",
                    "fieldOfStudyId": "",
                    "institutionName": "Punjab Institute of Computer Sciences",
                    "location": "Lahore",
                    "sortOrder": 3,
                },
            ],
            "experiences": [
                {
                    "jobTitle": "Technical Program Manager/Program Manager",
                    "startDate": "12/01/2015",
                    "endDate": "16/11/2021",
                    "description": "Baltimore, MD \n Project : Zbizlink \n Project Description : ZBizlink https : "
                    "www.zbizlink.com \n This SaaS-based solution contains approximately 16 "
                    "sub-projects and two web interfacing portals for end users. It is a fully "
                    "integrated solution using a Microsoft SharePoint Portal online for its document "
                    "repository and Microsoft Dynamics CRM 2016 for candidates tracking. It has a "
                    "normalized transactional database and a separate data warehouse for reporting, "
                    "analysis, and statistics. This solution contains high level features such as : \n "
                    "Vendors Management-Manage vendors' data and vendors' performance \n Procurement "
                    "Management-Locates and displays new proposal's RFP/RFR/RFQ etc. and "
                    "evaluates/scores vendors' proposal'submissions. \n Capture Management-Builds "
                    "proposal response templates and plugs in appropriate content, identifies proposal "
                    "team members, and enables collaboration among teams in order to submit successful "
                    "proposal responses. \n Dashboard and Reports-Provides various widgets that "
                    "provide information and drive dynamic collaboration, such as customized matrix "
                    "reports. \n Completed this project within a very tight timeline and budget. "
                    "Coordinated with team of 12 resources on a daily basis to ensure that all work "
                    "performed met expected results. It is quite an accomplishment for a team this "
                    "size, in this timeframe and with this budget to deliver a working software "
                    "product of this size and complexity. The application is getting very high marks "
                    "from business users. \n Other projects include data warehouses, portals, "
                    "architecture and development, conversion, configuration management, "
                    "change management, release management, and testing efforts. \n General "
                    "Responsibilities for all ZDAAS Projects \n Design and direct development of IT "
                    "strategy that supports company's strategic mission and business plan. Implement "
                    "and manage strategy across IT domain. \n Develop and ensure compliance to "
                    "corporate IT standards and policies to ensure compatibility and integration "
                    "throughout company. \n Configure, Install and manage Cloud environments 12 VM "
                    "Servers and three separate regions on Windows Azure for Zbizlink Production and "
                    "Test environments. Prepare always On and Azure Cloud as well as prepared backup "
                    "policies for VM backup, application backup, databases backups and environments "
                    "configurations backup. \n Developed Agile SCRUM artifacts including guidelines, "
                    "standards, and best practices to manage the development of ZBizlink. Oversees "
                    "adherence to, and use of development methodologies, frameworks, and project "
                    "tools. Supports and advises team on all technical and performance-impacting "
                    "issues. \n Strategically plan and manage initiatives consisting of program "
                    "components that meet stakeholder expectations. \n Report to Sr. Executive "
                    "Management; authorize and manage internal and external relationships and "
                    "dependencies across initiative components to ensure successful delivery of the "
                    "program. \n Ensure efficient distribution of the technical and business "
                    "resources; and will coordinate with business executives the initiation or "
                    "continuation of project based on business requirements, business performance and "
                    "available organizational resources. \n Responsible for establishing and executing "
                    "adequate project management controls based on industry accepted methodologies and "
                    "standards. \n Committed to monitor and control cost, schedule, performance and "
                    "risk; to ensure quality and security; overall integration and issues resolution "
                    "and to perform administrative functions. \n Co-ordinate with executive "
                    "management, prepare annual budget and spending strategies, and monitor business "
                    "and financial performance of initiative components from strategic perspective. \n "
                    "Attend and/or leads technical discussions/JAD sessions with application "
                    "designers, developer's, architects, business analysts, senior-level business "
                    "executives, and content strategists to develop complex designs, "
                    "business solutions, and management plans mapped to business demands. \n Manage "
                    "multiple projects and all project requirements-conduct functional and "
                    "non-functional requirements analysis; provides complex project and system "
                    "analysis. \n Manage day to day business tasks and client-driven assignments and "
                    "deliverables using PMI, PMBOK, and Agile development models including SCRUM . \n "
                    "Attend meetings; create and deliver status and project reports to client's and "
                    "their senior technical staff members; facilitates communication between all key "
                    "IT groups, business, and the customer community. \n Recruit and interview "
                    "resources; direct, train, and mentor all individuals and teams. Provides "
                    "governance and oversight. Manage multiple teams simultaneously. Verify and "
                    "validate work quality, timeliness and Agile compliance by resources. \n "
                    "Responsible for all design and development, including : \n Architecture - "
                    "Co-ordinate Microsoft Dynamics CRM architectural, integration parameters with "
                    "internal and external components including interfaces for Zbizlink with "
                    "SharePoint and CRM Dynamics. \n Enhancements, new features and upgrades "
                    "development, testing, deployment, maintenance \n QA/QC, validation and testing "
                    "including UAT \n Production support and maintenance of ongoing operations \n "
                    "Tools & Technology \n Microsoft Office, Microsoft Project, Microsoft Team "
                    "Foundation Server, Microsoft Dynamics CRM 2016 SharePoint 2016 Live, Vision, "
                    "Microsoft Framework 6.0, C#, Java, AngularJS, MVC 5.0, Entity Framework 5.0, "
                    "ASP.NET, SQL Server 2014.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 1,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "18/11/2013",
                    "endDate": "15/07/2015",
                    "description": "Project : Maryland Educators Information System EIS/MSDE \n Budget : $678, "
                    "450 \n Worked in collaboration with MSDE consultants and business users to "
                    "determine the gaps in requirements. Determined functionalities and defined "
                    "workable solutions to bridge gaps, designing the optimum technical solution in "
                    "the context of the client's environment, requirements, and financial resources. "
                    "Ensured the delivery of a quality system design which meets system performance "
                    "requirements, an effective human-machine interface, optimal operational cost, "
                    "and flexibility for future change. \n Responsibilities \n Defined the logical, "
                    "technical, and physical architecture for SharePoint as application platform that "
                    "are consistent with architecture principles, standards, methodologies, "
                    "and best practices. \n Implemented processes automation by creating Custom "
                    "Workflows Activities. \n Customizing Entity, Ribbon, Sitemap, Charts and "
                    "Dashboard in Dynamics CRM 2015. \n Created Custom scripts to migrate Dynamics CRM "
                    "4.0 to Dynamics CRM 2015. \n Analyzed architectural differences between different "
                    "solution methods and the challenges and approaches to integrating solutions built "
                    "on different platforms. \n Migrated 1.2 million Documents using Power Shell from "
                    "file system into SharePoint 2013. \n Created Workflows using Visual Studio 2013 "
                    "and SharePoint Designer 2013 for implementing different business rules. \n "
                    "Created Custom events for business data validation and SharePoint 2013 timer jobs "
                    "for scheduling events using Visual Studio 2013. \n Developed custom web parts to "
                    "update and retrieve Dynamics CRM 2015 entities data. \n Used Scribe Insight for "
                    "Dynamics CRM 4.0 data migration \n Designed and developed application framework "
                    "using ASP.Net, MVC5, MVVM, Entity, LinQ, HTML5, JavaScript and CSS3. \n Optimized "
                    "the Performance of the SharePoint 2013 server by configuring BranchCache and "
                    "creating indexing. \n Automated backup and restore processes for SharePoint "
                    "Content Databases by creating custom PowerShell Scripts. \n Implemented Single "
                    "sign on by implementing ADFS Active Directory Federation Services . \n Created "
                    "queues and relays using Azure Service Bus. \n Conducted interoperability with "
                    "on-premises line of business applications using WCF web services. \n Develop "
                    "custom web parts and integrating enterprise content with SharePoint to include "
                    "developing data repositories, content indexing and workflow. \n Tools & "
                    "Technology : JavaScript, .NET, ADX Studio, Scribe, Microsoft SharePoint 2013, "
                    "Visual Studio 2012, Microsoft Dynamics CRM 2015 and SQL Server 2012.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 2,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "10/10/2012",
                    "endDate": "18/11/2015",
                    "description": "Project : Maryland Accountability and Reporting System MARS \n Budget : $1.8 "
                    "Million and $12.24 Million \n Provided Project Management support to two vital "
                    "software application initiatives supporting the Maryland State Board of Education "
                    ": \n Maryland Accountability and Reporting System MARS which is used for State "
                    "agency users to manage the participating programs, payments, "
                    "and registrations/renewals. \n MARS Portal which is used Statewide for public "
                    "users agencies to participate in different foods/nutrition programs for school "
                    "system. This application developed in Microsoft Framework 2.0 but enhanced to "
                    "Framework 4.0 with C# language at backend. \n Responsibilities \n High "
                    "collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Offered great level "
                    "of collaboration with the finance department and various functional managers to "
                    "ensure IT operational budgets are properly estimated and controlled; provide "
                    "overall financial recommendations, and develop controls and measurements to "
                    "monitor progress. \n Developed, analyze and report IT resource requirements to "
                    "support objectives e.g., staffing, costs needed to meet objectives via resource "
                    "modeling efforts. Participates in and often may lead vendor management efforts "
                    "pertaining to sourcing. \n Facilitated communication between all key IT groups "
                    "and the customer community via participation in meetings and the creation of "
                    "status reporting mechanisms weekly, monthly, and quarterly . \n Supported the "
                    "Senior Technical Staff Members with regard to large scale initiatives through "
                    "resource modeling and providing complex analysis and reporting to Senior IT "
                    "management. \n Performed the code review, and measured the quality matrixes. \n "
                    "Monitored and controlled production supports, enhancements, QA/QC to ensure the "
                    "24/7 availability of applications. \n Coordinated with MSDE stakeholders to "
                    "conduct production support, UAT and ongoing operations. \n Prepared and delivered "
                    "weekly and monthly status reports, budget reports and performance reports. \n "
                    "Tools & Technology \n Microsoft Framework 4.0, C#, AngularJS, MVC 4.0, "
                    "Entity Framework 5.0, ASP.NET, SQL Server 2005.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 3,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "10/10/2012",
                    "endDate": "18/11/2015",
                    "description": "Project : Maryland Accountability and Reporting System MARS \n Budget : $1.8 "
                    "Million and $12.24 Million \n Provided Project Management support to two vital "
                    "software application initiatives supporting the Maryland State Board of Education "
                    ": \n Maryland Accountability and Reporting System MARS which is used for State "
                    "agency users to manage the participating programs, payments, "
                    "and registrations/renewals. \n MARS Portal which is used Statewide for public "
                    "users agencies to participate in different foods/nutrition programs for school "
                    "system. This application developed in Microsoft Framework 2.0 but enhanced to "
                    "Framework 4.0 with C# language at backend. \n Responsibilities \n High "
                    "collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Offered great level "
                    "of collaboration with the finance department and various functional managers to "
                    "ensure IT operational budgets are properly estimated and controlled; provide "
                    "overall financial recommendations, and develop controls and measurements to "
                    "monitor progress. \n Developed, analyze and report IT resource requirements to "
                    "support objectives e.g., staffing, costs needed to meet objectives via resource "
                    "modeling efforts. Participates in and often may lead vendor management efforts "
                    "pertaining to sourcing. \n Facilitated communication between all key IT groups "
                    "and the customer community via participation in meetings and the creation of "
                    "status reporting mechanisms weekly, monthly, and quarterly . \n Supported the "
                    "Senior Technical Staff Members with regard to large scale initiatives through "
                    "resource modeling and providing complex analysis and reporting to Senior IT "
                    "management. \n Performed the code review, and measured the quality matrixes. \n "
                    "Monitored and controlled production supports, enhancements, QA/QC to ensure the "
                    "24/7 availability of applications. \n Coordinated with MSDE stakeholders to "
                    "conduct production support, UAT and ongoing operations. \n Prepared and delivered "
                    "weekly and monthly status reports, budget reports and performance reports. \n "
                    "Tools & Technology \n Microsoft Framework 4.0, C#, AngularJS, MVC 4.0, "
                    "Entity Framework 5.0, ASP.NET, SQL Server 2005.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 4,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "04/10/2012",
                    "endDate": "30/08/2012",
                    "description": "Project : Needles Case Management System \n Budget : $278, 000 \n Director of "
                    "Software Engineering and Project Manager of the Needles Case Management System "
                    "project, a Power Builder application with some of the modules developed by using "
                    "VB Scripts. \n Responsibilities \n Prepared and submitted the Proposal, "
                    "demonstrated the Oral presentation to the client in order to win this contract. "
                    "\n High collaboration with IT management and IT colleagues to translate "
                    "corporate/functional business and information objectives into an IT "
                    "strategic/tactical business plan and systems development. \n Managed the project "
                    "deliverables by following industry best practices and Maryland State defined "
                    "standards. \n Managed day to day assignments, and verification of work done by "
                    "resources. \n High collaboration with business customers in examining solution "
                    "options and in planning and managing multiple IT centric projects. \n Consulted "
                    "within the IT organization to develop appropriate support for IT centric projects "
                    "from various technology and service departments; integrate activities with "
                    "business units, corporate departments, and IT departments to ensure the "
                    "successful implementation and support of project efforts. \n Managed the project "
                    "deliverables by using Agile and SPRINT development model, managed the day to day "
                    "assignments, and verified of work done by resources. \n Managed daily SCRUM "
                    "meetings and biweekly SPRINT meetings. \n Performed the code review, and measured "
                    "the quality matrixes. \n Made sure that team members successfully customized the "
                    "DevExpress and XtraReports library to intergrade Needles report objects to "
                    "provide complete solution for on-demand reports building. \n Achieved a complete "
                    "solution without requiring any design or specifications documents. \n \n Tools & "
                    "Technology \n Microsoft Framework 4.5, C#, Windows Presentation Foundation, Java, "
                    "DevExpress, XtraReports, NHibernate, Sybase, Windows Forms and TeamCity and "
                    "Microsoft Dynamics CRM 2011{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 5,
                },
                {
                    "jobTitle": "Project Manager",
                    "startDate": "01/09/2010",
                    "endDate": "30/09/2014",
                    "description": "Project : Subcabinet for Children Youth & Families Information System SCYFIS Web "
                    "Application Upgrade \n Budget : $2.2 Million \n Team Lead and Solutions Architect "
                    "of the SCYFIS Web Application Upgrade project on behalf of the State of "
                    "Maryland's Governor's Office for Children GOC . Served as the senior solutions "
                    "architect and involved in the development and successful implementation of the "
                    "upgrade. \n The SCYFIS web application was developed in 2003 to help Maryland "
                    "keep track of interagency services provided to children and their families. "
                    "SCYFIS primary users are case worker's, hospital worker's, State agencies, "
                    "service providers, and the general public. \n This initiative convenes the State "
                    "agencies, local partners, and community stakeholders to develop policies and "
                    "initiatives which reflect the priorities of the Governor and the Children's "
                    "Cabinet and resulting in improved services for Maryland's children and youth. \n "
                    "Responsibilities \n to upgrade the classic 'asp SCYFIS web application to .NET "
                    "platform I was involved to achieve the following : \n High collaboration with IT "
                    "management and IT colleagues to translate corporate/functional business and "
                    "information objectives into an IT strategic/tactical business plan and systems "
                    "development. \n Managed the project deliverables by following industry best "
                    "practices and Maryland State defined standards. \n Managed day to day "
                    "assignments, and verification of work done by resources. \n High collaboration "
                    "with business customers in examining solution options and in planning and "
                    "managing multiple IT centric projects. \n Consulted within the IT organization to "
                    "develop appropriate support for IT centric projects from various technology and "
                    "service departments; integrate activities with business units, corporate "
                    "departments, and IT departments to ensure the successful implementation and "
                    "support of project efforts. \n Completed the conversion of Crystal reports XII to "
                    "Crystal Reports 2008 and classic 'asp web application to .NET. \n Tools & "
                    "Technology \n Microsoft Framework 4.5, C#, ASP, MVC 4.0, Entity Framework 4.5, "
                    "SQL Server 2008, Knockout JS, JQuery, HTML 5 and Razor.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 6,
                },
                {
                    "jobTitle": "Technical Lead/IT Director",
                    "startDate": "01/01/2010",
                    "endDate": "18/11/2015",
                    "description": "Project : MDVOTERS II/III \n Director of Software Engineering and technical lead "
                    "started from project transition-in phase to ongoing maintenance and production. "
                    "\n Responsibilities \n Participated in contract transition-in phase and lead the "
                    "effort of the configuration of systems at new environments.\t \n Provided bugs "
                    "fixes and production support services to MDVOTERS II application. \n Provided "
                    "technical supervision to the developer's staff utilized by Canton Group. \n "
                    "Managed the project deliverables by using Agile and SPRINT development model "
                    "managed the day to day assignments, and verified of work done by resources. \n \n "
                    "Tools & Technology \n Microsoft Framework 4.5, VB.NET, Team Foundation Server, "
                    "Oracle 11g, and JIRA.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 7,
                },
                {
                    "jobTitle": "Technical Project Manager/Applications Architect",
                    "startDate": "01/07/2005",
                    "endDate": "31/08/2010",
                    "description": "Project : Managed and Lead more than 20 applications \n Technical Lead and "
                    "Enterprise Architect for a group of primarily .NET applications projects that "
                    "included but are not limited to tracking work activities, adoptions, "
                    "community emergency responses, welfare and social services systems and Maryland "
                    "Secretary's Mail Log. Successfully completed numerous projects, including "
                    "software for a real time interface between the Work Program System WORKS and the "
                    "Client Automated Resource and Eligibility System CARES, SAIL, OHEP, "
                    "Healthy Maryland, MARE, AdoptUsKids and development of reports for various "
                    "applications. \n Responsibilities \n Served as proficient Team Lead more than 20 "
                    "applications, including Cold Fusion, ASP, Delphi, MS Access, and .NET software. "
                    "\n Led at least 17 software professionals, including programmers, testers, "
                    "and technical writers. \n Contributed to and supervised the preparation of the "
                    "contents for Software Development Life Cycle SDLC and design specifications of "
                    "project deliverables. \n Prepared project schedules, project plans, "
                    "resource plans, scope plans, and unit test scripts. Track project schedule and "
                    "variances, activities, defects, issues, and resource assignments. \n Prepared "
                    "weekly and monthly status reports. Prepared and submitted CIO brief documents. \n "
                    "Participated in successful transition of hardware and software to a new Dallas, "
                    "Texas facility. \n Designed the architecture Framework for DHR .NET Applications, "
                    "which is currently used for high volume applications. \n Selected Projects \n "
                    "Work Program System WORKS \n The WORKS application was converted from DataFlex to "
                    ".NET platform. It has both Batch/RTI real time interface with CARES system. WORKS "
                    "serves the Marylander customers by enrolling in FDW/SD activities and tracks "
                    "their hourly attendance, sending auto-generation of Sanction letters to CARES and "
                    "stores Narratives for the customer benefit history. Monthly maintenance job EMR "
                    "to adjust the customer attendance hours as per the defined Federal policies and "
                    "eligibility requirements to maintain/improve the work participation rate. It "
                    "performs case assignments by alphabetical and customized order to the worker's "
                    "and as well as it measures the worker's work performance. \n Single Access "
                    "Interface Links SAIL \n This was the new application developed by using .NET "
                    "platform. It has both Batch/RTI real time interface with CARES system, "
                    "OHEP and Health Maryland System. This application provides single access to "
                    "Marylanders who needed support from Welfare systems by applying into any of "
                    "Maryland State's available Welfare systems. The interfaces with other systems "
                    "were established to transform and streamline the client's applications data. The "
                    "interfaces were developed under the concept of SOA framework and concepts. \n "
                    "Maryland Adoption Resource Exchange MARE System \n This application was converted "
                    "from old classic 'asp/VB Scripts to new .NET platform. This application is used "
                    "by Maryland State caseworker's to manage the child adoptions to and from the "
                    "families. A new interface was established with the U.S central database website "
                    "'AdoptUsKids org' to transfer the cases from Maryland State'system MARE to U.S "
                    "central database. \n Local Transaction Request System LTRS \n This application "
                    "was converted from Delphi to .NET 3.5 and MVC 2.0 platform. It is a critical "
                    "financial application. It used by the local Child Support offices to communicate "
                    "to the State Disbursement Unit SDU, a central office, all requests for financial "
                    "adjustments. It tracks the transaction requests made for local issues concerning "
                    "centrally posted payments. The supervisor processes or denies the requests and "
                    "records comments on the transaction request. It also tracks the age of the "
                    "transaction requests, the contact person, the original date of the request, "
                    "the transaction request type, the TAD representative assigned to the request, "
                    "the request status, and request comments and different reports. \n Local "
                    "Supervisory Surveys Instrument LSRI \n LSRI was revitalized from .NET 1.1 to .NET "
                    "platform and MVC 2.0 Framework. It tracks the employee surveys information and "
                    "provides the ability to edit the survey questions, responses, and response types. "
                    "\n Secretary's Mail Log SML \n SML application was converted from Delphi to .NET "
                    "3.5 and MVC 2.0 platform. This high profile application is used to send/track "
                    "mail notifications across the board. The reports and tasks/assignments serve the "
                    "local offices and employees. \n DHR Framework \n Articulated architectural "
                    "vision, conceptualized and experimented with alternative architectural "
                    "approaches, created models, blueprints, and validated the architecture against "
                    "requirements and assumptions. Studied the organization's goals, needs and given "
                    "the business objectives of the organization and created technology roadmaps, "
                    "made assertions about technology directions and determined their consequences for "
                    "the technical strategy and hence architectural approach. The following areas : "
                    "business units, project services, development, data modeling, database designing, "
                    "and organization's infrastructure were deeply considered during the development "
                    "of the enterprise solution. Designed the architecture and directed the developing "
                    "of .NET Framework for DHR. \n The additional responsibilities for the framework "
                    "development were : \n Created Object Role Model ORM Diagram \n Analysis "
                    "Mechanisms \n Class Responsibility Collaborator CRC Model Class \n Class Diagrams "
                    "\n Participated in development and implementation \n Instructed the technical "
                    "writers to document the how to consume framework during the development of future "
                    "applications \n Led the project with all SDLC responsibilities started from "
                    "analysis to implementation phase \n Tools & Technology \n ASP.NET 2.0, C#, "
                    "SQL Server 2005, Java Script, DHTML, T-SQL & Stored Procedures, Microsoft .NET "
                    "Framework 2.0 and Visual Studio.Net 2005 \n Hospital Billing System \n "
                    "Implemented a Hospital Billing System for Humanim Inc. that allowed users "
                    "including hospital personnel including billing staff, case managers, "
                    "and physicians to submit insurance claims and receive money online. This "
                    "application tracks the submitted claims for the individual customers and "
                    "collected funds. This application complies with HIPPA standards for filling "
                    "charts, and complete codes such HICF 1500, SB92, and CPT to charge insurance "
                    "companies. This application was developed by using Cold Fusion, Java Scripts and "
                    "SQL Server 2000. \n Welcome Maryland Website \n Programmed Welcome MD State "
                    "application for tourism services. It was developed into both ASP and ASP.NET "
                    "platforms. The classic ASP was used to modify the existing site with new design "
                    "and features. ASP.NET/C# was used to provide the feature of content management of "
                    "the site. It provided the flexibility to the administrators for updating/editing "
                    "the contents of complete site.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 8,
                },
                {
                    "jobTitle": "Director of Software Engineering",
                    "startDate": "04/12/2004",
                    "endDate": "18/11/2015",
                    "description": "{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 9,
                },
                {
                    "jobTitle": "Programmer Analyst",
                    "startDate": "01/09/2002",
                    "endDate": "31/01/2004",
                    "description": "Baltimore, MD \n Client : Bermuda Tourism \n Project : Bermuda Tourism In & "
                    "Outbound Call Management \n This application was developed to automate the "
                    "conversion between CSRs Customer Services Representatives and one of the "
                    "multi-nation Company's potential customers through an outbound call process "
                    "system. The code was developed to automate and track outbound telemarketing "
                    "initiatives. The information parsing module was written to review and analyze the "
                    "provided information through inbound calls by the customers/callers and then "
                    "screened the calls which were received with maximum information. An automatic SQL "
                    "scheduled job was developed to send out HTML generated emails to "
                    "callers/customers to make the calls successful. \n Responsibilities \n Developed "
                    "inbound call queue receives calls from customers callers either by telephone or "
                    "by web. \n Developed the outbound call queue to response the calls from inbound "
                    "call queue. \n Wrote the stored procedures to make the inbound call list, "
                    "outbound call list and outbound call queue. \n Wrote stored procedure and SQL Job "
                    "scheduling scripts to send automated dynamic emails to callers. \n Developed the "
                    "ASP pages, form validating scripts. \n Integrated completed website \n Wrote test "
                    "cases, test scripts. \n Performed unit testing, integrating testing. \n \n Tools "
                    "& Technology \n ASP VB Scripts, Visual Basic, SQL Server 2000, Erwin, "
                    "Java Script, HTML/DHTML, Microsoft .NET Framework, T-SQL & Stored Procedures, "
                    "Windows/Web Authentication Solutions, CSS and FrontPage Extensions.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 10,
                },
                {
                    "jobTitle": "Team Leader/Project Coordinator",
                    "startDate": "01/05/2000",
                    "endDate": "30/04/2002",
                    "description": "Baltimore , MD \n Client : Bermuda Tourism \n \n This application was developed "
                    "to automate the conversion between CSRs Customer Services Representatives and one "
                    "of the multi-nation Company's potential customers through an outbound call "
                    "process system. The code was developed to automate and track outbound "
                    "telemarketing initiatives. The information parsing module was written to review "
                    "and analyze the provided information through inbound calls by the "
                    "customers/callers and then screened the calls which were received with maximum "
                    "information. An automatic SQL scheduled job was developed to send out HTML "
                    "generated emails to callers/customers to make the calls successful. \n "
                    "Responsibilities \n Developed inbound call queue receives calls from customers "
                    "callers either by telephone or by web. \n Developed the outbound call queue to "
                    "response the calls from inbound call queue. \n Wrote the stored procedures to "
                    "make the inbound call list , outbound call list and outbound call queue. \n Wrote "
                    "stored procedure and SQL Job scheduling scripts to send automated dynamic emails "
                    "to callers. \n Developed the ASP pages , form validating scripts. \n Integrated "
                    "completed website \n Wrote test cases , test scripts. \n Performed unit testing , "
                    "integrating testing. \n \n Tools & Technology \n ASP VB Scripts , Visual Basic , "
                    "SQL Server 2000 , Erwin , Java Script , HTML/DHTML , Microsoft .NET Framework , "
                    "T-SQL & Stored Procedures , Windows/Web Authentication Solutions , "
                    "CSS and FrontPage Extensions. \n Team Leader/Project Coordinator 05/2000 - "
                    "04/2002 \n M.M. Tech Pvt. Ltd.{#}",
                    "clientName": "",
                    "projectName": "",
                    "tools": "",
                    "sortOrder": 11,
                },
            ],
            "requests": [
                {
                    "type": "Minimum Qualifications",
                    "sortOrder": 0,
                    "queries": [
                        {
                            "sortOrder": 1,
                            "query": "A minimum of six (6) years of experience in User Acceptance Testing.",
                        },
                        {
                            "sortOrder": 2,
                            "query": "A minimum of two (2) years of experience leading teams of software testers.",
                        },
                        {
                            "sortOrder": 3,
                            "query": "A minimum of four (4) years of experience in development of automation scripts "
                            "using Selenium, Selenium Web Driver, QTP, Python or similar tools. ",
                        },
                        {
                            "sortOrder": 4,
                            "query": "A minimum of four (4) years of experience in writing SQL queries with strong "
                            "knowledge of database concepts. ",
                        },
                        {
                            "sortOrder": 5,
                            "query": "A minimum of two (2) years of experience in developing automated scripts for "
                            "RESTful services and integrating them with Jenkins/GIT. ",
                        },
                        {
                            "sortOrder": 6,
                            "query": "A minimum of two (2) years of experience in testing websites across multiple "
                            "browsers, testing web-services, back-end processing and data validation "
                            "utilizing SQL. ",
                        },
                        {
                            "sortOrder": 7,
                            "query": "Strong testing and analytical skills with keen attention to details.",
                        },
                        {"sortOrder": 8, "query": "Experience in Quality Assurance (QA) related functions."},
                        {
                            "sortOrder": 9,
                            "query": "Proven experience working effectively and collaboratively with stakeholders "
                            "from multiple functional teams in an organization. ",
                        },
                    ],
                },
                {
                    "type": "Preferred Qualifications",
                    "sortOrder": 10,
                    "queries": [
                        {
                            "sortOrder": 11,
                            "query": "A minimum of four (4) years of experience as a JAVA/Web application tester on "
                            "complex and dynamic, multi-agency technology projects within the healthcare "
                            "industry. ",
                        },
                        {
                            "sortOrder": 12,
                            "query": "A minimum of four (45) years of experience leading teams of software testers "
                            "performing manual and/or automation testing. ",
                        },
                        {"sortOrder": 13, "query": "Hands-on experience with SQL, HTML, CSS and JavaScript."},
                        {
                            "sortOrder": 14,
                            "query": "Hands-on experience with backend database testing on DB2, SQL, PostgreSQL or "
                            "any other enterprise database systems. ",
                        },
                        {
                            "sortOrder": 15,
                            "query": "Strong technical testing skills using SQL to perform complex DB queries.",
                        },
                        {"sortOrder": 16, "query": "Experience with defect-tracking/management tools such as JIRA."},
                        {
                            "sortOrder": 17,
                            "query": "Experience in testing or supporting State Based Marketplace or healthcare "
                            "systems. ",
                        },
                        {"sortOrder": 18, "query": "Experience with EDI 834 and Medicaid 8001 transactions."},
                        {
                            "sortOrder": 19,
                            "query": "Demonstrated experience with industry standard Quality Assurance best practices "
                            "for Agile and Iterative SDLCs, testing methodologies, version control systems, "
                            "implementation, and deployment activities. ",
                        },
                        {
                            "sortOrder": 20,
                            "query": "Experience in system testing, data warehouse migration testing, data integrity "
                            "testing and data transformation related testing. ",
                        },
                    ],
                },
            ],
        }

    def test_create_parser(self):
        """
        :Message: creation of task
        :return: None
        """
        data = json.dumps(self.data, indent=4)

        url = "http://127.0.0.1:8000/api/parser/"
        response = requests.post(url, data=data, headers=self.headers, auth=None)
        import socket

        print("me ithe wa-->", socket.gethostbyname(socket.gethostname()))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class GetKeywordByIDTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()

    def test_get_keyword_by_id(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"/api/keyword-management/{self.keyword.pk}/"
        print(url, self.keyword.pk)
        response = self.client.get(path=url)
        print("id-->", response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetKeywordByIdInvalidIdTestCase(APITestCase):
    def setUp(self):
        """
        :return: None
        """
        super().setUp()
        self.keyword_tag = KeywordTag(name="test s dDf")
        self.keyword_tag.save()
        self.keyword = Keyword(keyword_value="test value", keyword_tag=self.keyword_tag)
        self.keyword.save()

    def test_update_keyword(self):
        """
        :Message: for getting specific task
        :return: None
        """
        url = f"{'/api/keyword-management/190/'}"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
