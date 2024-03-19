<!-- MIT License

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. -->
<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Command-line Application Suite</h3>

  <p align="center">
    A command-line based menu system with various applications.
    <br />
    <a href="https://github.com/PalD777/CmdMenuSuite"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href=https://github.com/PalD777/CmdMenuSuite/issues">Report Bug</a>
    ·
    <a href="https://github.com/PalD777/CmdMenuSuite/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The Command-line Application Suite aims to provide an intuitive menu system using curses, such that a user is easily able to view and run various scripts. We have tried to make the addition of new scripts as simple as possible so that the menu is easily expandable.

<p align="right">(<a href="#top">back to top</a>)</p>



### Demo

<img src="demo.gif">

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy of the application suite up and running follow these steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PalD777/CmdMenuSuite.git
   ```
2. Install necessary libraries
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* To run:
    ```
    python3 main.py
    ```
* To add a script:
  1. Place your script in the `Scripts` folder.
  2. Import `os.system` and `sys.executable` in the script.
  3. Call `os.system(f'"{sys.executable}" main.py')` once the script is done.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PalD777/CmdMenuSuite.svg?style=for-the-badge
[contributors-url]: https://github.com/PalD777/CmdMenuSuite/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PalD777/CmdMenuSuite.svg?style=for-the-badge
[forks-url]: https://github.com/PalD777/CmdMenuSuite/network/members
[stars-shield]: https://img.shields.io/github/stars/PalD777/CmdMenuSuite.svg?style=for-the-badge
[stars-url]: https://github.com/PalD777/CmdMenuSuite/stargazers
[issues-shield]: https://img.shields.io/github/issues/PalD777/CmdMenuSuite.svg?style=for-the-badge
[issues-url]: https://github.com/PalD777/CmdMenuSuite/issues
[license-shield]: https://img.shields.io/github/license/PalD777/CmdMenuSuite.svg?style=for-the-badge
[license-url]: https://github.com/PalD777/CmdMenuSuite/blob/master/LICENSE.txt
