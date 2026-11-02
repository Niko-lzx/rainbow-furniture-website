# 技术 SEO 仓库检查（2026-11-02）

范围：`Niko-lzx/rainbow-furniture-website`，默认分支 main，基线提交 `6b870a7fee2a4108ab80c4d2f07095250d324997`。递归检查全部 29 个 HTML、robots.txt、sitemap.xml、README 和仓库文件清单。仓库没有 AGENTS.md、CNAME 或自定义部署工作流；README 明确称本项目为“官网样板站”。因此不能证明与生产站一致。

## 已确认的仓库问题与最小修复

- 25 个 HTML 缺少 canonical；原有 4 个（首页和 3 个产品详情页）均为 HTTPS、www 域名，且与站点地图相符。补齐其余页面的单个 head 内自引用 canonical；首页继续使用 `/`。
- 内部编写说明不只存在于机场案例：还涉及首页搜索入口/关键词策略、知识库标题与页脚、文章页 SEO Article 标签、工厂落地页 SEO Landing Page 标签、案例页素材补充要求、产品库建设说明、产品页关键词栏目、产品中心字段补齐、服务流程标题、关于页新版官网说明和检测页的官网排版建议。仅替换这些文字或删除内部说明段落，不改布局、CSS、图片、路径或导航。
- 不虚构项目名称、现场交付资料、电话、地址、检测认证或产品参数。删除 contact 页“正式上线时放置联系方式”的制作说明；保留“样板站表单暂不提交数据”的功能提示，避免使客户误以为表单已接通。

## 站点地图与 robots 检查

- sitemap.xml XML 可解析，29 个 loc 无重复，与 29 个 HTML 的规范地址一一对应；无指向仓库不存在页面的条目。
- robots.txt 允许全站抓取，唯一 Sitemap 声明与仓库 sitemap 地址一致。
- 未发现可由仓库证据确认的地图/robots 地址错误，因此两个文件保持不变。未添加未经证实的 lastmod 日期，也未切换 www 或非 www。
- 仓库 HTML 内部链接目标存在。此结论只指文件存在，不代表线上返回 200 或可被索引。

## 验证

运行 `python scripts/check_seo.py`：29 HTML pages; 29 sitemap URLs; 0 errors。
运行 `git diff --check`：通过。
校验覆盖：canonical 数量、head 位置、HTTPS 主机及逐页地址、首页根地址、地图重复/缺页/多余地址、robots 地图声明、全站禁爬、HTML 相对链接、已识别内部文案模式。
文案模式检查不能替代人工审核；本次另用关键词检索逐项复查。保留文件名/图片目录/CSS 类里的 seo，不将实现名称当作面向客户的文案。

## 待线上验证（本次未确认、未部署）

1. 由部署负责人确认生产站来自哪个仓库、分支、提交及发布目录；特别核对样板站与当前正式站是否为同一套代码。
2. 读取 HTTP/HTTPS × www/非 www 的响应链、证书和最终 URL，确认首选域名及永久重定向。现有 www 口径仅为仓库一致性选择，不是生产域名结论。
3. 对首页、全部 28 个子页、robots.txt、sitemap.xml 检查最终状态码、重定向、实际源代码 canonical、HTTP Link/X-Robots-Tag，以及 HTML robots/noindex；确认不存在软 404、跨页 canonical 或被屏蔽路径。
4. 对比服务器返回的 sitemap/robots 与本仓库；确认地图中的 URL 均可访问、可索引并直接返回首选地址。生产站可能有本仓库以外的页面，不能用本仓库地图覆盖它。
5. 在站长平台验证抓取/索引与搜索引擎选择的 canonical；本次离线检查不证明收录、排名或流量变化。
6. 上线前补充经核实的真实案例详情、客户联络渠道并接通表单；这些属于内容真实性/转化完整度问题，当前补丁不编造资料或实现后台。

## 逐页 canonical 清单

“新增”表示基线缺失后补齐；“保留”表示原有配置正确。本清单仅针对仓库。

| 页面 | 基线→补丁 | canonical |
|---|---|---|
| about.html | 新增 | https://www.rainbowfurniture.com.cn/about.html |
| article-airport-furniture.html | 新增 | https://www.rainbowfurniture.com.cn/article-airport-furniture.html |
| article-executive-office-furniture.html | 新增 | https://www.rainbowfurniture.com.cn/article-executive-office-furniture.html |
| article-factory-showroom.html | 新增 | https://www.rainbowfurniture.com.cn/article-factory-showroom.html |
| article-foshan-office-furniture-factory.html | 新增 | https://www.rainbowfurniture.com.cn/article-foshan-office-furniture-factory.html |
| article-healthcare-furniture.html | 新增 | https://www.rainbowfurniture.com.cn/article-healthcare-furniture.html |
| article-office-chair-manufacturer.html | 新增 | https://www.rainbowfurniture.com.cn/article-office-chair-manufacturer.html |
| article-office-furniture-solutions.html | 新增 | https://www.rainbowfurniture.com.cn/article-office-furniture-solutions.html |
| article-school-furniture-project.html | 新增 | https://www.rainbowfurniture.com.cn/article-school-furniture-project.html |
| articles.html | 新增 | https://www.rainbowfurniture.com.cn/articles.html |
| case-airport-furniture-project.html | 新增 | https://www.rainbowfurniture.com.cn/case-airport-furniture-project.html |
| case-education-furniture-project.html | 新增 | https://www.rainbowfurniture.com.cn/case-education-furniture-project.html |
| case-government-office-project.html | 新增 | https://www.rainbowfurniture.com.cn/case-government-office-project.html |
| case-healthcare-furniture-project.html | 新增 | https://www.rainbowfurniture.com.cn/case-healthcare-furniture-project.html |
| case-office-furniture-project.html | 新增 | https://www.rainbowfurniture.com.cn/case-office-furniture-project.html |
| cases.html | 新增 | https://www.rainbowfurniture.com.cn/cases.html |
| contact.html | 新增 | https://www.rainbowfurniture.com.cn/contact.html |
| executive-office-furniture.html | 新增 | https://www.rainbowfurniture.com.cn/executive-office-furniture.html |
| foshan-office-furniture-factory.html | 新增 | https://www.rainbowfurniture.com.cn/foshan-office-furniture-factory.html |
| index.html | 保留 | https://www.rainbowfurniture.com.cn/ |
| office-chair-manufacturer.html | 新增 | https://www.rainbowfurniture.com.cn/office-chair-manufacturer.html |
| office-chair-products.html | 新增 | https://www.rainbowfurniture.com.cn/office-chair-products.html |
| office-furniture-solutions.html | 新增 | https://www.rainbowfurniture.com.cn/office-furniture-solutions.html |
| product-cm-b142as-51.html | 保留 | https://www.rainbowfurniture.com.cn/product-cm-b142as-51.html |
| product-cm-b356asg-1.html | 保留 | https://www.rainbowfurniture.com.cn/product-cm-b356asg-1.html |
| product-cm-f85as-1.html | 保留 | https://www.rainbowfurniture.com.cn/product-cm-f85as-1.html |
| products.html | 新增 | https://www.rainbowfurniture.com.cn/products.html |
| quality.html | 新增 | https://www.rainbowfurniture.com.cn/quality.html |
| solutions.html | 新增 | https://www.rainbowfurniture.com.cn/solutions.html |
