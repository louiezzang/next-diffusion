# next-diffusion
---


# Requirements
python >= 3.8

# Development Environment (Optional)
This is for setting up your IDE development environment.
The `[packages]` section in `Pipfile` will be automatically updated according to `requirements.txt` file.
```
$ pipenv install --skip-lock -r requirements.txt 
```
To activate this project's virtualenv
```
$ pipenv shell
```

# Build Package
```
$ python3 setup.py bdist_wheel
```

# References
- Huggingface Diffusers 
    https://github.com/huggingface/diffusers/tree/main/examples/
- Jeremy Howard’s Course of From Deep Learning Foundations to Stable Diffusion
    https://www.fast.ai/posts/part2-2022-preview.html  
    Lesson 9: Deep Learning Foundations to Stable Diffusion, 2022 (https://youtu.be/_7rMfsA24Ls)
    https://github.com/fastai/diffusion-nbs

