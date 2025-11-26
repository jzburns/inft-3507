# INFT-3507 / INFT-6000 Principles of Distributed Systems
### Homework 2 Assignment
## Content-Based Subscriptions Using Google Cloud Pub/Sub (Regex Filtering)


## Overview
In this assignment, you will implement a distributed messaging system using **Google Cloud Pub/Sub**. The goal is to demonstrate **content-based subscription**, where subscribers decide whether to process a message based on the *content of the message body*.

Because Google Pub/Sub does **not** natively support filtering on message bodies, you will build subscribers that:

- Pull all messages from a shared topic  
- Examine each message’s text  
- Apply **regular expression (regex)** rules  
- Print only the messages that match their assigned patterns  

The publisher simply emits messages; the subscribers implement the content-based behavior.

## GCP Project
1. You may only use GCP pub-sub for this project
1. By now you should all be added to ``inft-3507`` or very soon, added to ``inft-6000``,
therefore, I prefer you all work in this project
1. If you already have your own GCP account and project
configured correctly, you may use this if you wish

## What You Will Build

### 1. Publisher
You will write a publisher that:

- Iterates over each line of ``logs.csv``, and for each
topic (``WARN, ALERT, DEBUG, INFO, ERROR``), 
publishes the text following the topic to that topic.
- For example, the publisher would publish  the plaintext **Refreshed session token for user438** to the ``DEBUG`` topic
- When the publisher gets to the end of the ``logs.csv``
it should start back at the top.
- The publisher should sleep for 2 seconds before publishing to the next topic.

The publisher does **not** filter or classify messages — it just publishes them.

### 2. Subscribers (Content-Based Filtering)
You will create **four subscribers**, each configured with its own set of **regex rules**.

Each subscriber should:

1. Load its regex rules from a configuration file (YAML or JSON). The file is called ``rules.json`` or ``rules.yaml`` whichever format you want to use
2. Connect to the same Pub/Sub topic as the publisher  
3. Pull every message  
4. Parse the message text  
5. Apply its set of regex patterns  
6. Print the message **only if it matches at least one rule**  

This work simulates **content-based subscriptions** layered on top of Pub/Sub’s topic-based delivery model.

## Dynamic Rule Loading
To demonstrate dynamic configuration in distributed systems:

- Each subscriber must **reload its rules file periodically** (e.g., every 10 seconds).  
- If a rule changes or new rules are added, the subscriber should pick up the change *without restarting*.  

This lets you test adjustments to filtering behavior at runtime.


## Input Files

### 1. Log File
Please use ``logs.csv`` - you do **not** need to create your own log files.

### 2. Rules File (`rules.json` or `rules.yaml`)
Each subscriber has an entry containing **six regex rules**, for example:

```yaml
subscribers:
  "2":
    - level: INFO
      pattern: "User user[0-9]{3} reset MFA"
    - level: WARN
      pattern: ".*brute-force.*"
```

1. subscriber #2 subscribes to the ``INFO`` topic
and filters for text that contains ``"User user[0-9]{3} reset MFA"``
1. subscriber #2 also subscribes to the ``WARN`` topic
and filters for ``".*brute-force.*"``


## What You Will Demonstrate

- Topic-based distribution using Pub/Sub  
- **True content-based subscription** implemented at the subscriber level  
- Configuration-driven subscriber behavior  
- Dynamic reloading of rules  
- Semantic filtering based on message meaning  


## A note on Topic Creation and Topic Naming

1. Because we will have many students attempting this 
assignment, they cannot all use the topic name ``DEBUG, WARN`` etc.
1. When you create your topic (which you can do in the console, or at the command line (see Bonus)), make
sure you give them a unique topic name
1. For example, for gmail_id ``jb72997@gmail.com`` you can create a topic called ``WARN-jb72997``, ``DEBUG-jb72997`` etc.


## Deliverables
These deliverables **must** be placed into the 
github classrooms private repo. No other approach
will be accepted.

### 1. Source Code

- Publisher program  
- Four subscriber programs

### 2. Sample Output

Include:

- Subscriber output showing matches  
- Evidence that rule changes take effect dynamically  

### 3. Youtube hosted (delisted) video  (min 10 mins)

``README.md`` containing the URL for a Youtube hosted (delisted) video
Explain:
- What content-based subscription means  
- Why Pub/Sub does not support it natively  
- How your implementation achieves it  
- How dynamic rule loading works

**This video must demonstrate understanding of the code you present**


## Grading (100 pts)

| Category | Points |
|---------|--------|
| Publisher implementation including file read and sleep | 25 |
| Subscriber filtering logic using Regex | 25 |
| Subscriber Dynamic rule reloading | 25 |
| Quality and accuracy of the video discussion | 25 |

## Bonus
Write a script/program to automate the creation and deletion of the topics for your code. 
For example:

```
./script.sh setup
```
will cause your topics and subscriptions to be created by the script/code.

and of course, the ``teardown``

```
./script.sh teardown
```
will cause all your topics and subscriptions to be deleted by the script/code.

**Use whichever programming language/script you want**

Should you wish to attempt the bonus question, you must show evidence of this working in your 
``README.md`` and commit the code to your github repo.

(**+ up to 3% extra, giving a maximum of 13%**)

## Warning
1. **_If any part of your submission contains suspicious content, you will receive a grade of 0._**. 
1. **_For your information, I define suspicious as also including similarity with the work of others as 
well as including AI or other assisted elements_**.
1. **_You have been warned._**. 
