## ember 余烬
研一上半学期 刘继飞老师 《神经网络与深度学习》课程的作业代码

ONNX（Open Neural Network Exchange）是一种开放格式，用于表示深度学习模型。它旨在促进不同框架之间的模型共享和互操作性。ONNX模型的导出协议允许开发者将训练好的模型从一种深度学习框架转换成ONNX格式，之后可以导入到其他支持ONNX的框架中进行推理或进一步的处理。

本项目基于PyTorch实现了一个简单的神经网络，并将其导出为ONNX格式。

项目结构：

- `model.py`：定义了卷积神经网络模型
- `train.py`：训练模型并保存参数
- `export.py`：将模型导出为ONNX格式
- `onnx_inference.py`：使用ONNXRuntime库进行推理
- `onnx_inference_with_trt.py`：使用TensorRT库进行推理

运行方式：

```
# 训练模型并保存参数
python train.py

# 导出模型为ONNX格式
python export.py

# 使用ONNXRuntime库进行推理
python onnx_inference.py

# 使用TensorRT库进行推理
python onnx_inference_with_trt.py
```