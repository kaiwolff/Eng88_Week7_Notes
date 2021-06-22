## Intro to DevOps

### What is DevOps good for?

Before DevOps, Development and Testing/QA were separate entities. This proved to have some problems as the isolated nature meant each of Dev, Testing, and Operations didn't get the "full picture" of what they were working on, Devops aims to address this problem by integrating the processes so that Development and Operations are combined (hence the name DevOps).

The Application Design Patterns have changed from "monolithic" approaches to a split between backend/devops and frontent, or a microservice based approach, where severals product services are aggregated and presented to the user via a frontend. This limits the effect of bugs (as the microservices exist in separate areas), and limit downtime. it also stops the "all-or-nothign" approach to a project, as each service can be added separately without affecting the other services' functionality.

### Microservices

Microservices are an organisational structure, where each microservice is designed to handle a specific process. They can interact with each other if needed.



While Agile methodology is well suited to being integrated into DevOps, the two are separate. it is also possible to wokr with DevOps principles and use, for example, the waterfall development method.

### Challenges for a DevOps Engineer

- Ease of use
- Flexibility
- Robustness
- Cost

Ease of use is vitla as other teams will be reusing software to work on later. When building somethign, it is important that it is easy to use by either a customer or by other developments. By putting effort into making parts easy to use, time is saved as code can more easily be reused.

Flexibility is similarly important as it aims to make the repurposing of parts of a developers code easier. As practices in the sector constantly evolve and new technologies are developed, it is important to attempt to make it possible to migrate to new technologies as they emerge, avoiding being "locked in" to a particular software, for example.

Robustness - it is important to eliminate single points of failure, so that osoftware is not broken by an error in an unrelated part of the program if possible. This is, for exampel, acheived by ringfencing microservices so that they can operate independently of each other if necessary

Cost -0 This is an often-overlooked aspect of development. For example, using machines that don't use more capacity than necessary. Making sure that the resources used are as close as possible to the resources required by the services.


### Relationship between Agile and DevOps

DevOps is broadly based on Agile principles. By breakign things down into smaller parts and deploying/delivering more frequently, risks are reduced and the process lends itself to, for example, repeated sprints as employed by the Scrum method, as a sprint might cover aspects relating to a particular microservice.

### DevOps

Hard to define specifically, as there is much discussion on how to define the concept. However, can agree on some practical definitions:

- A collaboration of Development and operations
- A culture promoting collaboration between Development and Operations tea to deploy code to production faster in automated and repeatable ways.
- A practice of development and operation engineers taking part in the whole service lifecycle together
- An approach that allows quicker and more reliable development of superior quality software

Academic deifnition

"A set of practices intended to reduce the time between committing a change to a system and the change being placed into normal production, while ensuring high quality."


 ## CAMS model
Core concept of devops:
- culture
    - Devops starts with learning how to work differently. Embracing cross-functional teams that interact with transparency, respect and openness, so that each team knows what hte other one is working on. This is similar to the Agile approaches previously discussed
- Automation
    - A very important part of DevOps, as having systems in place to replicate errors. In a nutshell, if there are more than three commands that are run on a very regular basis, it's better to have a bash script to do them for you. Reduces room for human error, as a working configuration, if put into automation, will mean the correct approach is being reliably taken at that point. Having polcieis and standards that can be automated using scripts and software is a useful part of this, for example automated testing with Jenkins
- Measurement
  - By monitoring and trackign performance throughout the cycle, the need to rework is limited. The goal is to expect errors, and ensure they are not repeated if possible. This lowers the cost of production significantly by lowering the number of reworks needed
- Sharing
    - Usually, people hide their problems because they think they will be punished or blamed for them. By sharing problems and mistakes, it is however possible for everyone to learn more quickly. The key is to have a blame-free environment as mistakes occur naturally and are more easily solved if they are quickly brought to everyone's attention
    

Key Aim of DevOps is to get the working product into the hands of customers as quickly as possible. This may take the shape of having, for example, monthly updates to software, which gives the customer a working product earlier and then adds features on. This leans on the above CAMS model.

### DevOps Principles

- Customer-Centric Action
    - customer should be taken into consideration in all steps. Need to focus on producing a product that can be sold to/used to by customers with a high degree of customer satisfaction. Steps taken should be done with teh aim of contributing to increased customer satisfaction.
    
- End-to-End Responsibility
    - Need to provide updates or product support until the software reaches end-of-life. Notice that end-of-life does not ncessarily mean end-of-use, and it may occasionally be necessary to release patches if a huge vulenrability is discovered after a product has ceased receiving official support. Important to this is gfood documentation so that past steps can be retraced if needed
    
- Continuous Improvement
    - Focus on continually doing things in a better way.
-Automate Everything
      - Automation is vital for the DevOps process. Not only for the software development side, but for the entire landscape. Ideally automate everything, from testing, to creating or destroying infrastructure, configuring firewalls, etc.The more can be automated, the more time developers can spend on adding value to the product rather than repeating themselves taking testing steps.
- Work as one team
    - In DevOps culture roles, there should be no isolated positions. While specialisation can be helpful, full collaboration should be the norm, and specialists shoudl be available of what the rest of the team are doign and vice versa
- Monitor and Test Everything
    - In order to improve, need to constantly monitor performance and requirements from the customer side.
    
### DevOps Lifecycle

- Continuous Development
- Continuous Testing
- Continuous Integration
- Continuous deployment
- Continuous Monitoring

Notice that all parts are continuos throughout the.

Testing - Once the initial code has been created, it will be continuously tested for bugs, either while unchanged and certainyl more rigorously before any new features are accepted. Can use automation for this e.g. Selenium.

Integration - Heart of processes. Requires developers to commit changes to the source code more frequently. Each commit is then built, unit-tested, integration-tested and packaged.

Deployment - Stage where tested and integrated new code is sent intot he production environment. It is important here to ensure that the code is correctly deployed to all servers in such a manner that any change made should not compromise the functionality of the application.

Monitoring - Once deployed, performance, customer feedback and use cases need to be gathered and reviewed so that the information cna beused to target improvements to future releases. The more information is gathered, the better. For example, by monitoring if performance degrades after a new release, it is possible to address this problem before app functionality is compromised.


## Tools

A lot available, mostly concerned with aiding the automation of stagesa of this cycle. For example, Jenkins helps to automate testing of committed code. Ties into setting up an evnironment, using several toolsets to create the architecture of the project



### Risk Register

List possible risk areas, including an estimate of how likely the even it to happen, and the severity of the impact of an event occuring.

In conclusion:
DevOps impacts the culture, affecting the entire development process. It has become the favoured approach for almost all IT departments, with demand far outstripping supply, especially in the DevSecOps area. This is especially true with the Covid-19 pandemic, which caused more needs for secure remote access to company infrastructures as employees had to work from home due to the quarantine.

CI/CD

Continuous Integration - Coding philosophy/ set of practices. Drive to implement small changes and check in code to version control more often. Aim is ot establish consistent, automated way of building, packaging and testing applications. With consistency in integration process, teams are likely to commit more frequently, leading to better colaboration and software quality

Continuous Deployment - automate the delivery of applications to production environment, or other selected ifnrastructure. 



The principles of CI/CD are part of the DevOps Lifecycle. 

Cannot always have continuous delivery. In some sectors, lengthy testing is required before deployment is permitted.

WHY CI/CD

 - Reduce cost
- Faster Release Rate
- Smaller Code Changes
- Fault Isolation
- Reliable testing
- Increased transparency & accountability
- Easy maintenance and updates