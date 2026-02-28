"""
XUnity LLM Translate
大模型翻译工具主程序
"""

from ui.app import TranslationServiceApp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translation Service App")
    
    parser.add_argument("-start", "--start", action="store_true", help="自动开始运行服务")
    
    args = parser.parse_parser()

    app = TranslationServiceApp()

    if args.start:
        app.run(auto_start=True)
    else:
        app.run()
