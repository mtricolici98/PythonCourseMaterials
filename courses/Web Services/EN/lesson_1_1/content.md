## Why do we need external packages

Often, we feel overwhelmed by the complexity of real world applications, and how much programming logic goes into making
things that seem very simple to the user.

The reality is, that most of the work has already been done before us, by other programmers. They have managed to
structure a solution in such a way that makes it very easy for other programmers to use it to be closer to a finished
result, without needing to know all the ins and outs of how it actually works underneath.

To provide a similar example, imagine that it wouldn't make sense for everyone who wants to drive a car, that they know
how to make a car. Instead, you but a car that is already made, and learn how to drive it, sometimes you even learn how
to make small maintenance on the car, but you are able to get to where you want to be by using work that someone else
has done to make a good car.

External packages are what makes working with python shine in new colors, and it is extremely easy to get started on
using them.

### There are many packages

The world of python packages is extremely developed, and this gives you plenty of options to chose from in all areas of
development.

For example, in web development, the Python ecosystem offers a plethora of packages catering to diverse needs and
preferences. Flask and Django stand out as two prominent frameworks, each with its own philosophy and feature set.
Flask, known for its minimalist design and flexibility, empowers developers to craft lightweight, customizable web
applications with ease. On the other hand, Django embraces a "batteries-included" approach, providing a comprehensive
suite of tools and conventions for building robust, scalable web projects.

In addition to frameworks, a myriad of specialized packages augment the web development experience. Libraries like
Requests simplify HTTP communication, enabling seamless integration with external APIs and services. Meanwhile,
SQLAlchemy streamlines database interactions, offering an expressive and intuitive interface for working with relational
databases.

Moreover, the advent of asynchronous programming has spurred the emergence of asyncio and Trio, empowering developers to
build high-performance, non-blocking web applications. These asynchronous frameworks leverage Python's coroutines and
event loops to handle concurrent operations efficiently, unlocking new possibilities for real-time communication and
resource utilization.

Beyond web development, the Python package ecosystem extends its reach into domains such as data science, machine
learning, and artificial intelligence. Libraries like NumPy, Pandas, and Scikit-learn furnish data scientists with
powerful tools for data manipulation, analysis, and predictive modeling. Similarly, TensorFlow and PyTorch empower
researchers and practitioners to implement cutting-edge machine learning algorithms and neural network architectures
with ease.

Furthermore, Python's versatility extends to areas such as game development, desktop applications, and system
administration, thanks to libraries like **Pygame**, **PyQt**, and **Fabric**. Whether you're building immersive gaming
experiences, crafting intuitive user interfaces, or automating system tasks, Python's rich ecosystem of packages equips
developers with the tools they need to bring their ideas to life.

In summary, the abundance of Python packages reflects the vibrancy and diversity of the programming community. By
leveraging these libraries and frameworks, developers can accelerate development, foster innovation, and push the
boundaries of what's possible in software engineering.

## How to get started

Pick a domain that you are interested in, whether it's web development, data science, machine learning, or any other
field where Python finds its application. Understanding your interests and aspirations will guide you in selecting the
right tools and resources to embark on your journey.

When you have picked the right domain, it would be easier for you to find the tools you need to actually get the work
done. There are many resources, and many community discussion that will aid you in finding the right way to do things,
but an important aspect is to do something that **feels right** to you.

If you want to make a web-service in python, you can start off by searching for a small guide online, usually, you will
find that the tutorials use one of the following: Flask, Django, FastAPI or some other tool. These tools, are also
called frameworks.

### What are frameworks

Frameworks in the programming context, stand out as being a set of tools that offer all the building blocks necessary
for you to just worry about the logic of the construction of your service, without having to worry about more in-depth
knowledge that comes with that.

Think of it as when trying to build a piece of furniture: Using a framework is like building furniture you bought from
IKEA, where you are given all the tools and parts, thus you can just go ahead and build your furniture, without needing
to know how to mill or machine metal, process wood or make glass.

Once you have got a feeling of what the framework actually does. You can dive deeper into it by reading its
documentation.

### The documentation

Documentation is an essential part of a library, as it ensures that the functionality of the library is clearly
explained to the programmers who intend to use it, and the ways you can interact with the library are expressed with
proper examples and descriptions.

Documentation for large projects (such as [Django](https://docs.djangoproject.com/en/5.0/)) can be very extensive, but
they usually have a **Quick Start Guide**, or a **Getting Started** page, that will show you quickly on how you can
start building your stuff.

You can also think of the documentation as the _User manual_ of a library, and most libraries come with at least a small
set of documented functions and processes.

## Managing your packages

It is normal when working with a large software, that you end up collecting a lot of packages on which your project
**depends**. They are so-called **dependencies**, and without them your project will likely not run, and you will end
up seeing many "**ModuleNotFound**" errors.

In order to ease the process of managing these dependendcies (installing, updating, etc...) the programming world
invented a piece of software called a **Package Manager**.

In Python, the package manager is called PIP, and it allows us to install, remove, update and save our dependencies in a
easy and accessible way.

## PIP

PIP is a command-line tool that allows Python developers to install, uninstall, and manage software packages written in
Python. It serves as the de facto standard for package management in the Python community and is included by default
with Python installations from version 3.4 onwards.

**How to Use PIP:**

1. **Installation:**
   Before you can start using PIP, ensure that you have Python installed on your system. Most modern Python
   distributions come with PIP pre-installed. To check if PIP is installed, open a terminal or command prompt and type:
   ```
   pip --version
   ```
   If PIP is installed, you'll see the version number; otherwise, you'll need to install Python first.

2. **Installing Packages:**
   Installing packages with PIP is straightforward. To install a package, use the following syntax:
   ```
   pip install package_name
   ```
   Replace `package_name` with the name of the package you want to install. For example, to install the popular NumPy
   package for numerical computing, you would type:
   ```
   pip install numpy
   ```
   PIP will download the package from the Python Package Index (PyPI) repository and install it on your system.

3. **Listing Installed Packages:**
   You can view a list of all installed packages and their versions by running the command:
   ```
   pip list
   ```
   This command will display a list of installed packages along with their version numbers.

4. **Upgrading Packages:**
   To upgrade a package to the latest version, use the following command:
   ```
   pip install --upgrade package_name
   ```
   This command will upgrade the specified package to the latest version available on PyPI.

5. **Uninstalling Packages:**
   If you no longer need a package, you can uninstall it using the following command:
   ```
   pip uninstall package_name
   ```
   Replace `package_name` with the name of the package you want to uninstall. PIP will remove the package and its
   dependencies from your system.

6. **Installing Packages from Requirements Files:**
   You can also install packages listed in a requirements file using PIP. To do this, create a text file (
   e.g., `requirements.txt`) containing a list of package names and versions, each on a separate line. Then, run the
   following command:
   ```
   pip install -r requirements.txt
   ```
   PIP will install all the packages listed in the requirements file.

7. **Virtual Environments:**
   Virtual environments allow you to create isolated Python environments for your projects, each with its own set of
   packages and dependencies. To create a virtual environment, navigate to your project directory and run the command:
   ```
   python -m venv myenv
   ```
   Replace `myenv` with the name of your virtual environment. To activate the virtual environment, run the appropriate
   command for your operating system:
    - On Windows:
      ```
      myenv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source myenv/bin/activate
      ```
   Once activated, you can use PIP to install packages within the virtual environment without affecting your system-wide
   Python installation.

### What are requirement files

Requirement files, are often used by programmers to specify all the dependencies of a project in one file, often when
working with Python Projects, you will see a file called `requirements.txt`. This means that the developer who worked on
the project has stored all of his dependencies in one file, so it would be easy for other developer to also set-up the
project to continue working.

You can create a requirement file using PIP. The command bellow will generate a requirements file from all the currently
installed dependencies.

```
pip freeze > requirements.txt
```