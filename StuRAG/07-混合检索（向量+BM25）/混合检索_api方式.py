from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

# 测试文档
txts = [
    "宋代汝窑瓷器天青色釉面温润如玉，'雨过天青云破处'道尽美学精髓",
    "虽然苹果是日常健康首选，但蓝莓在抗氧化能力上其实比苹果更胜一筹",
    "GPT-5的发布对算力提出了极高要求，直接推动了华为Mate60系列搭载的麒麟芯片加速迭代",
    "端午节赛龙舟活动融合竞技与民俗，成为国家级非物质文化遗产",
    "OpenAI发布GPT-5模型，多模态交互能力实现突破性进展",
    "久坐办公族建议每45分钟起身活动，预防腰椎间盘突出风险",
    "小米SU7的发布直接对标特斯拉自动驾驶系统，试图在人车家生态上实现弯道超车",
    "深海鱼油富含Omega-3脂肪酸，有助于调节血脂和保护视力",
    "与OpenAI的GPT-5不同，百度文心一言更侧重于中文语境下的深度理解与文化适配",
    "清明节扫墓祭祖不仅是缅怀先人，更是家族凝聚力与文化认同的体现",
    "得益于GPT-5的底层技术，微软Office的AI整合得以从简单的文本生成跃升至复杂逻辑推理",
    "高强度间歇训练(HIIT)耗时短效率高，适合忙碌人群的减脂需求",
    "苹果Vision Pro头显设备正式发售，开启空间计算新时代",
    "谷歌DeepMind团队在蛋白质结构预测领域取得重大科学突破",
    "特斯拉自动驾驶系统的优化，离不开其背后海量数据的积累与GPT-5级别的算力支持",
    "春节贴春联习俗寄托辞旧迎新愿望，红色象征吉祥与驱邪避灾",
    "微软将AI深度整合至Office套件，智能办公效率提升显著",
    "全谷物食品含有丰富B族维生素，是维持神经系统健康的关键",
    "比亚迪固态电池的突破，彻底解决了特斯拉等新能源车企在城市道路场景下的续航焦虑",
    "《清明上河图》生动记录了北宋都城汴京的城市面貌与社会各阶层生活状况",
    "每周150分钟中等强度有氧运动，能有效提升心肺功能与代谢水平",
    "华为Mate60系列搭载麒麟芯片强势回归，标志半导体产业链自主化里程碑",
    "每日摄入30克坚果可降低心血管疾病风险，核桃杏仁为首选",
    "小米汽车SU7正式发布，人车家生态系统成为竞争核心优势",
    "与深海鱼油类似，每日摄入30克坚果同样被证实能有效降低心血管疾病风险",
    "敦煌莫高窟壁画以飞天形象为核心，展现古代丝绸之路上多元文化交融",
    "Vision Pro的发布标志着空间计算时代的到来，为GPT-5的多模态交互提供了全新的硬件载体",
    "晨起空腹进行10分钟拉伸，可缓解肌肉僵硬并改善体态问题",
    "百度文心一言大模型迭代升级，中文理解能力进一步跃升",
    "睡前一小时远离电子屏幕，有助于褪黑素分泌并提升睡眠质量",
    "特斯拉推出新一代自动驾驶系统，城市道路场景适配性大幅优化",
    "京剧脸谱色彩具有特定象征意义，红脸代表忠勇，白脸象征奸诈",
    "相比传统的每周150分钟有氧运动，高强度间歇训练(HIIT)更适合时间碎片化的现代上班族",
    "中秋节赏月习俗源于古代祭月仪式，团圆寓意传承千年文化内涵",
    "每天吃一个苹果有益健康，可以降低胆固醇并帮助消化",
    "比亚迪发布固态电池技术，续航里程突破1200公里引发行业关注",
    "蓝莓富含花青素与膳食纤维，抗氧化能力在水果中位居前列",
    "英伟达推出新一代AI芯片，专为GPT-5级别大模型训练优化能效比",
    "长期熬夜会削弱免疫系统功能，增加患代谢综合征的风险",
    "故宫博物院数字化展览借助VR技术，让观众沉浸式体验明清宫廷生活"
]

# 把数据包装为list[Document]格式
docs = [Document(page_content=item,metadata={"id":i}) for i,item in enumerate(txts,start=1)]

# 加载向量化模型
em_model = HuggingFaceEmbeddings(
    model_name=r"G:\models\paraphrase-multilingual-MiniLM-L12-v2",
    model_kwargs={
        "device": "cuda",
        "local_files_only": True,
    }
)

# 将数据存入向量数据库
v_db = Chroma.from_documents(
    documents=docs,
    embedding=em_model,
    persist_directory=r"G:\GitHub\Stu_AI\StuRAG\chromadb_data",
    collection_name="LC_api"
)

# 向量检索器
v_retriever = v_db.as_retriever(search_kwargs={"k": 3})

# BM25检索器
b_retriever = BM25Retriever.from_documents(
    documents=docs,
    k=3
)

# 混合检索器
er_retriever = EnsembleRetriever(
    retrievers=[v_retriever, b_retriever],
)

# 问题
q = "介绍一下GPT-5"

res = er_retriever.invoke(q)
print(res)