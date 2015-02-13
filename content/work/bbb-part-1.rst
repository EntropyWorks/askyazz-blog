BBB == Big Bang Base (Part 1)
#############################

:Authors: Yazz D. Atlas
:slug: BBB-part-1
:category: Work 
:date: 2015-02-12 12:49
:tags: deployment, devops, vagrant, virtualbox
:summary: Thoughs on how to create a common development environment.

You ever have a project that you want to work on with other? For me its
all the time. I was normally the guy in the background setting up that 
environment for the developers to run on. That has changed in the last 
10 years with the increase use of virtualization. Now developers are 
deploying temporary virtual machines and containers instead.  Which can
make life much easier for me. But not all the time. 

Why
---

Creating a common development environment is a key feature to success in
my opinion. Without it you can was hours trouble shooting a problem one 
developer has with while nobody else is. From choosing the wrong version 
of software to wrong expectations of operating system. There are so many
variables to be addressed.

Gathering Data
--------------

Before starting a project with multiple contributors a few guidelines need 
to be setup. Mostly for me this is the time I discover how simple or complex
a project is. It is not unheard of a team of developers requesting multiple servers, 
a replicated database, caching, NoSQL, queuing, etc. So I will start there with
a simple list of questions.

    - Servers
          - Number of each kind
                - Web server
                - Application
                - Database
                - Load balancer
                - Caching
                - Queuing
                - Other
          - Operating Systen
                - Version + Release
                - Particular package repositories
          - Storage
                - Estimated application
                - Estimated data        
                - Estimated log + rention period
          - Base install requirement
                - Version of packages needed
                - How is development code put into production
                - Ports that need to be open or secured
          - Networking
                - Public IP ranges
                - Private IP ranges
                - Number of network interfaces
                - VLANS
                - BONDING

Thats enought normally to get a basic idea of the layout of the environment. Each itme there
I bet someone could write a book on if they wanted to. This also isn't a
complete list by anyones standard.

But What about Virtualzation
----------------------------

Thats for my next post...
