<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/radioactive11/vinyl-server">
  </a>

  <h3 align="center">Vinyl</h3>

  <p align="center">
    Skribble for Music.  
    <br />
    <br />
    <a href="https://github.com/kg-kartik/moonlight-client/">Frontend</a>
    ·
    <a href="https://github.com/kg-kartik/vinyl-server-backend/">User Backend</a>
    ·
    <a href="https://vinyl-server.radioactive11.com">View Demo</a>
    ·
    <a href="https://github.com/radioactive11/vinyl-server/issues">Report Bug</a>
    ·
    <a href="https://github.com/radioactive11/vinyl-server/issues">Request Feature</a>
  </p>
</div>

<img src="STATIC/repo.png">


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Vinyl is a multiplayer song guessing game in which the first one (three people actually) to guess the name of the song from its 30 second preview wins. 

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With
<p>
<img alt="FastAPI" src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img alt="FastAPI" src="https://img.shields.io/badge/celery-37814A?style=for-the-badge&logo=celery&logoColor=white"/>
<img alt="FastAPI" src="https://img.shields.io/badge/redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
<img alt="Flask" src="https://img.shields.io/badge/mongodb-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
<img alt="Next" src="https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=next.js&logoColor=white"/>
<img alt="NodeJS" src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=node.js&logoColor=white"/>
<img alt="NodeJS" src="https://img.shields.io/badge/linode-00A95C?style=for-the-badge&logo=linode&logoColor=white"/>
</p>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you can setup your own game environment.

### Prerequisites

* Python>=3.7
* Redis
* NodeJS
* Next.js
* SQLAlchemy



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/radioactive11/vinyl-server.git
   ```
2. Create and activate virtual environment
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the requirements
   ```sh
   python3 -m pip install -r requirements.txt
   ```
4. Set PYTHONPATH environment variable
   ```sh
   export PYTHONPATH=app
   ```
5. Start the server
```sh
uvicorn main:app
```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## How to play

Playing vinyl is easy and simple. All you need to do is:

1. Create a room 🏠
2. Invite some friends (using the invite link) 💌
3. Choose your Spotify playlist (or from our Handpicked ones )🤌🏽
4. Choose the number of rounds 🔢
5. Guess the song before everyone else 🏆

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->

See the [open issues](https://github.com/radioactive11/vinyl-server/issues) for a full list of proposed features (and known issues).

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



<!-- CONTACT -->
## Contact

- [Arijit Roy](https://github.com/radioactive11/)
- [Kartik Goel](https://github.com/kg-kartik/)
- [Manavendra Sen](https://github.com/manavendrasen)
- [Somil Gupta](https://github.com/somil24)
- [Boidushya Bhattacharyay](https://github.com/boidushya)

Project Link: [https://vinyl-server.radioactive11.com](https://vinyl-server.radioactive11.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/radioactive11/vinyl-server.svg?style=for-the-badge
[contributors-url]: https://github.com/radioactive11/vinyl-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/radioactive11/vinyl-server.svg?style=for-the-badge
[forks-url]: https://github.com/radioactive11/vinyl-server/network/members
[stars-shield]: https://img.shields.io/github/stars/radioactive11/vinyl-server.svg?style=for-the-badge
[stars-url]: https://github.com/radioactive11/vinyl-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/radioactive11/vinyl-server.svg?style=for-the-badge
[issues-url]: https://github.com/radioactive11/vinyl-server/issues
[license-shield]: https://img.shields.io/github/license/radioactive11/vinyl-server.svg?style=for-the-badge
[license-url]: https://github.com/radioactive11/vinyl-server/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/arijit--roy
[product-screenshot]: images/screenshot.png