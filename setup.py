import os
import re

# 导入setuptools模块中的find_packages和setup函数
from setuptools import find_packages, setup

# 定义获取版本号的函数
def get_version():
    # 打开项目中的__init__.py文件以读取版本信息
    with open(os.path.join("src", "llmtuner", "__init__.py"), "r", encoding="utf-8") as f:
        file_content = f.read()  # 读取文件内容
        pattern = r"{0}\W*=\W*\"([^\"]+)\"".format("__version__")  # 定义搜索版本号的正则表达式
        (version,) = re.findall(pattern, file_content)  # 使用正则表达式查找版本号
        return version  # 返回找到的版本号

# 定义获取依赖列表的函数
def get_requires():
    # 打开requirements.txt文件以读取依赖信息
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()  # 读取文件内容
        # 提取所有非注释行并去除前后空白字符
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines  # 返回依赖列表

# 定义额外的依赖包分组
extra_require = {
    "deepspeed": ["deepspeed>=0.10.0"],
    "metrics": ["nltk", "jieba", "rouge-chinese"],
    # 更多的依赖组可以按需添加
    "unsloth": ["torch==2.2.0", "unsloth[cu121-ampere-torch220]"],
    "galore": ["galore-torch"],
    "badam": ["badam"],
    "vllm": ["vllm>=0.3.3"],
    "bitsandbytes": ["bitsandbytes>=0.39.0"],
    "gptq": ["optimum>=1.16.0", "auto-gptq>=0.5.0"],
    "awq": ["autoawq"],
    "aqlm": ["aqlm[gpu]>=1.1.0"],
    "qwen": ["tiktoken", "transformers_stream_generator"],
    "modelscope": ["modelscope"],
    "quality": ["ruff"],
}

# 定义主函数
def main():
    setup(
        name="llmtuner",  # 包名
        version=get_version(),  # 版本号
        author="hiyouga",  # 作者
        author_email="hiyouga@buaa.edu.cn",  # 作者邮箱
        description="Easy-to-use LLM fine-tuning framework",  # 包描述
        long_description=open("README.md", "r", encoding="utf-8").read(),  # 长描述，通常是README
        long_description_content_type="text/markdown",  # 长描述的内容类型
        keywords=["LLaMA", "BLOOM", "Falcon", "LLM", "ChatGPT", "transformer", "pytorch", "deep learning"],  # 关键词
        license="Apache 2.0 License",  # 许可证
        url="https://github.com/hiyouga/LLaMA-Factory",  # 项目URL
        package_dir={"": "src"},  # 包目录
        packages=find_packages("src"),  # 使用find_packages自动发现子包
        python_requires=">=3.8.0",  # Python版本要求
        install_requires=get_requires(),  # 安装时需要安装的依赖
        extras_require=extra_require,  # 额外的依赖
        classifiers=[  # 分类器
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    )

# 如果这段代码是一个典型的Python项目的安装脚本，
#采用了`setuptools`模块来配置和安装Python包。它主要用于设置一个名为`llmtuner`的Python库，该库专注于大型语言模型（LLM）的微调。


