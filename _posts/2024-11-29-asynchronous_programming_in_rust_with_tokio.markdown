---
layout: post
title: Asynchronous Programming in Rust with Tokio
date: 2024-11-29 14:48:00 +0200
description: Asynchronous Programming in Rust with Tokio
lang: en
img: post_images/rust_tokio.png
tags:
  [
    "rust",
    "threading",
    "multiprocessing",
    "async",
    "mutex",
    "semafor",
    "deadlock",
    "starvation",
  ]
contents:
  - "Asynchronous Programming in Rust with Tokio;asynchronous-programming-in-rust-with-tokio"
  - "Getting Started with Tokio;getting-started-with-tokio"
  - "Basic Example;basic-example"
  - "What Does #[tokio::main] Do?;what-does-tokiomain-do"
  - "Running Blocking and Asynchronous Tasks;running-blocking-and-asynchronous-tasks"
  - "Key Concepts;key-concepts"
  - "Unit Testing Asynchronous Code;unit-testing-asynchronous-code"
  - "Synchronization Primitives;synchronization-primitives"
  - "Mutex;mutex"
  - "Semaphore;semaphore"
  - "Notify;notify"
  - "Advanced Concepts;advanced-concepts"
  - "Barrier;barrier"
  - "RwLock;rwlock"
---

# Asynchronous Programming in Rust with Tokio

This document provides a comprehensive guide to using Rust's **Tokio** library for asynchronous programming. It covers fundamental concepts, code examples, and advanced usage techniques.

---

## Getting Started with Tokio

### Basic Example

The `#[tokio::main]` macro simplifies setting up an asynchronous runtime. Below is a simple example:

```rust
async fn hello_world() -> String {
    "Hello World".to_string()
}

#[tokio::main]
async fn main() {
    let value = hello_world().await;
    println!("{}", value);
}
```

### What Does `#[tokio::main]` Do?

- **Copies code from the main function**.
- **Starts an asynchronous runtime**.
- **Executes the code within this runtime**.

Here’s a manual setup without the macro:

```rust
fn main() {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .unwrap()
        .block_on(async {
            println!("Hello World!");
        });
}
```

---

## Running Blocking and Asynchronous Tasks

Sometimes, blocking tasks and async tasks need to coexist. Here's how to handle them:

```rust
use std::{thread, time};

use tokio::time::{sleep, Duration};

fn blocking_call() -> String {
    thread::sleep(time::Duration::from_secs(5));
    "Finally done".to_string()
}

async fn async_call(id: i32) {
    sleep(Duration::from_secs(1)).await;
    println!("Async Call: ID {}", id);
}

#[tokio::main]
async fn main() {
    let blocking_call_handle = tokio::task::spawn_blocking(blocking_call);

    let mut async_handles = Vec::new();
    for id in 0..10 {
        async_handles.push(tokio::spawn(async_call(id)));
    }

    for handle in async_handles {
        handle.await.unwrap();
    }

    let result = blocking_call_handle.await.unwrap();
    println!("Blocking call result: {}", result);
}
```

### Key Concepts

- **Blocking Tasks**: Use `tokio::task::spawn_blocking` to execute tasks in a separate thread, ensuring other async tasks remain unaffected.
- **JoinHandle**: Acts as a bridge between a spawned task and the main thread, giving access to the task's return value.

---

## Unit Testing Asynchronous Code

Testing async code requires specialized setup. Here's how:

```rust
#[tokio::test]
async fn test_add() {
    assert_eq!(async_add(1, 1).await, 2);
}
```

To control threading during tests, you can use:

```rust
#[tokio::test(flavor = "multi_thread", worker_threads = 1)]
```

---

## Synchronization Primitives

### Mutex

A `Mutex` ensures mutual exclusion, allowing only one task to access data at a time.

```rust
use tokio::sync::Mutex;

#[tokio::main]
async fn main() {
    let tv_channel = 10;
    let remote = Mutex::new(tv_channel);

    {
        let mut lock = remote.lock().await;
        *lock = 42;
    }

    println!("Updated channel: {}", *remote.lock().await);
}
```

**Thread-Safe Mutex**: Combine `Mutex` with `Arc` for shared ownership across tasks.

---

### Semaphore

Limits access to a shared resource for a fixed number of tasks.

```rust
use std::sync::Arc;
use tokio::sync::Semaphore;
use tokio::time::{sleep, Duration};

async fn teller(semaphore: Arc<Semaphore>, name: String) {
    let permit = semaphore.acquire().await.unwrap();
    println!("{} is being served", name);
    sleep(Duration::from_secs(2)).await;
    println!("{} is done", name);
    drop(permit);
}

#[tokio::main]
async fn main() {
    let semaphore = Arc::new(Semaphore::new(4));
    let mut tasks = Vec::new();

    for i in 0..10 {
        tasks.push(tokio::spawn(teller(semaphore.clone(), format!("Customer {}", i))));
    }

    for task in tasks {
        task.await.unwrap();
    }
}
```

---

### Notify

Allows tasks to notify others about events.

```rust
use std::sync::Arc;
use tokio::sync::Notify;
use tokio::time::{sleep, Duration};

async fn deliver_package(notify: Arc<Notify>) {
    sleep(Duration::from_secs(5)).await;
    println!("Package delivered!");
    notify.notify_one();
}

async fn wait_for_package(notify: Arc<Notify>) {
    notify.notified().await;
    println!("Package received!");
}

#[tokio::main]
async fn main() {
    let notify = Arc::new(Notify::new());

    tokio::spawn(deliver_package(notify.clone()));
    tokio::spawn(wait_for_package(notify.clone()));
}
```

---

## Advanced Concepts

### Barrier

Ensures all tasks reach a synchronization point before proceeding.

```rust
use std::sync::Arc;
use tokio::sync::Barrier;

#[tokio::main]
async fn main() {
    let barrier = Arc::new(Barrier::new(3));

    let mut tasks = Vec::new();
    for i in 0..3 {
        let barrier_clone = barrier.clone();
        tasks.push(tokio::spawn(async move {
            println!("Task {} waiting at the barrier.", i);
            barrier_clone.wait().await;
            println!("Task {} passed the barrier.", i);
        }));
    }

    for task in tasks {
        task.await.unwrap();
    }
}
```

---

### RwLock

Allows multiple readers or a single writer for shared data.

```rust
use std::sync::Arc;
use tokio::sync::RwLock;

#[tokio::main]
async fn main() {
    let lock = Arc::new(RwLock::new(String::from("Initial data")));

    let readers = (0..3).map(|_| {
        let lock = lock.clone();
        tokio::spawn(async move {
            println!("Reader: {}", *lock.read().await);
        })
    });

    let writer = {
        let lock = lock.clone();
        tokio::spawn(async move {
            let mut write_guard = lock.write().await;
            *write_guard = String::from("Updated data");
        })
    };

    futures::future::join_all(readers.chain(std::iter::once(writer))).await;
}
```

---

## Channels

Tokio supports communication between tasks through channels. Examples include `mpsc` (multi-producer, single-consumer) and `broadcast`.

---

This guide provides a solid foundation for building robust and scalable asynchronous applications with Rust's Tokio library. Explore the code snippets, experiment, and enhance your Rust async programming skills!
