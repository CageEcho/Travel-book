# Travel-book

把旅行行程做成一本可以翻的小书。打开后先看到书架，点开书就能像翻真书一样一页页看：两侧是扇形叠放的页，可以点击、拖动、滚轮或方向键翻页。

现在的示例是一份虚构的客户方案 **土耳其 12 日**（伊斯坦布尔 → 卡帕多奇亚 → 安塔利亚），共 28 页：封面、路线图、每日行程、美食、交通票据、报价、出发须知、确认步骤、封底。

> 演示样本：客户、日期、价格和顾问信息都是虚构的。

## 直接看

打开 `dist/土耳其12日-翻书旅行方案.html`。这是一个单独的文件，照片和字体都打包在里面，发给别人用浏览器打开就能看，不联网也能正常显示。电脑上效果最好，手机建议横屏。

## 项目结构

| 路径 | 内容 |
|---|---|
| `index.html` | 源文件：页面内容、版式和翻书效果都在这里 |
| `images/` | 原始照片和 `credits.json`（每张照片的出处与许可） |
| `scripts/fetch_fonts.sh` | 下载用到的开源字体到 `fonts/` |
| `scripts/build.py` | 压缩照片、裁剪字体，打包成 `dist/` 里的单文件 |
| `scripts/fetch_imgs.py` | 当初从 Wikimedia Commons 查找照片用的脚本 |
| `dist/` | 打包好的成品 |

## 修改内容后重新打包

页面内容在 `index.html` 的 `PAGES` 数组里，每一项是一页。改完以后：

```bash
./scripts/fetch_fonts.sh                 # 只需第一次
python3 -m venv .venv && .venv/bin/pip install fonttools brotli
PATH=.venv/bin:$PATH .venv/bin/python scripts/build.py
```

照片压缩用的是 macOS 自带的 `sips`；其他系统会直接复制原图，成品文件会大一些。

直接用浏览器打开 `index.html` 也能预览，只是字体要联网从 Google Fonts 加载。

## 照片出处

照片均来自 Wikimedia Commons，按各自的知识共享许可使用。使用 CC BY / CC BY-SA 许可的照片需要署名，BY-SA 的衍生作品需以相同许可发布。页面里点底部“···”按钮也能看到这份清单。

| 文件 | 原图 | 作者 | 许可 |
|---|---|---|---|
| `antalya_cliff.jpg` | [Antalya Lara Cliff view.jpg](https://commons.wikimedia.org/wiki/File:Antalya_Lara_Cliff_view.jpg) | My-view2U | CC BY-SA 4.0 |
| `avanos.jpg` | [In pottery shop in Avanos, Cappadocia, Turkey, May, 2015.jpg](https://commons.wikimedia.org/wiki/File:In_pottery_shop_in_Avanos,_Cappadocia,_Turkey,_May,_2015.jpg) | Alexey Komarov | CC BY-SA 4.0 |
| `balik.jpg` | [Vendeurs de balik ekmek (1).jpg](https://commons.wikimedia.org/wiki/File:Vendeurs_de_balik_ekmek_(1).jpg) | Jpbazard Jean-Pierre Bazard | CC BY-SA 3.0 |
| `bluemosque.jpg` | [Courtyard of the Blue Mosque, Istanbul. (54505628417).jpg](https://commons.wikimedia.org/wiki/File:Courtyard_of_the_Blue_Mosque,_Istanbul._(54505628417).jpg) | Mustang Joe | CC0 |
| `boat.jpg` | [From Bosphorus cruise sightseeing boat - panoramio.jpg](https://commons.wikimedia.org/wiki/File:From_Bosphorus_cruise_sightseeing_boat_-_panoramio.jpg) | Laima Gūtmane (simka… | CC BY-SA 3.0 |
| `bosphorus.jpg` | [Bosphorus panorama with bridge from Kiz Kulesi Istanbul 2024.jpg](https://commons.wikimedia.org/wiki/File:Bosphorus_panorama_with_bridge_from_Kiz_Kulesi_Istanbul_2024.jpg) | Furkan Akkurt | CC BY-SA 4.0 |
| `breakfast.jpg` | [Istanbul (29).jpg](https://commons.wikimedia.org/wiki/File:Istanbul_(29).jpg) | Mostafameraji | CC BY 3.0 |
| `cap_balloons.jpg` | [Balloons over Goreme.JPG](https://commons.wikimedia.org/wiki/File:Balloons_over_Goreme.JPG) | José Luiz | CC BY-SA 3.0 |
| `cap_pano.jpg` | [Cappadocia Balloon Inflating Wikimedia Commons.JPG](https://commons.wikimedia.org/wiki/File:Cappadocia_Balloon_Inflating_Wikimedia_Commons.JPG) | Benh LIEU SONG (Flickr) | CC BY-SA 3.0 |
| `cavehotel.jpg` | [View over Goreme from Sunset Cave Hotel Terrace - Goreme - Cappadocia - Turkey (5760943819).jpg](https://commons.wikimedia.org/wiki/File:View_over_Goreme_from_Sunset_Cave_Hotel_Terrace_-_Goreme_-_Cappadocia_-_Turkey_(5760943819).jpg) | Adam Jones from Kelowna, BC, Canada | CC BY-SA 2.0 |
| `cover.jpg` | [Süleymaniye Mosque, Istanbul, 20260606 0805 1307.jpg](https://commons.wikimedia.org/wiki/File:S%C3%BCleymaniye_Mosque,_Istanbul,_20260606_0805_1307.jpg) | Jakub Hałun | CC BY 4.0 |
| `dolma_ext.jpg` | [Pond and Fence along the Bosporus Strait, Dolmabahçe Palace, Istanbul.jpg](https://commons.wikimedia.org/wiki/File:Pond_and_Fence_along_the_Bosporus_Strait,_Dolmabah%C3%A7e_Palace,_Istanbul.jpg) | Julian Lupyan | CC0 |
| `dolma_gate.jpg` | [Dolmabahçe Palace and Sultans gate april 19 2014.jpg](https://commons.wikimedia.org/wiki/File:Dolmabah%C3%A7e_Palace_and_Sultans_gate_april_19_2014.jpg) | This Photo was taken by Wolfgang Moroder.  

Feel free to use my photos, but ple | CC BY-SA 3.0 |
| `dolma_in.jpg` | [Chandelier inside Dolmabahçe Palace, Istanbul.jpg](https://commons.wikimedia.org/wiki/File:Chandelier_inside_Dolmabah%C3%A7e_Palace,_Istanbul.jpg) | Julian Lupyan | CC0 |
| `ferry.jpg` | [Kadikoey, Istanbul (P1100156).jpg](https://commons.wikimedia.org/wiki/File:Kadikoey,_Istanbul_(P1100156).jpg) | Matti Blume | CC BY-SA 4.0 |
| `galata2.jpg` | [Galata Tower January 2015.JPG](https://commons.wikimedia.org/wiki/File:Galata_Tower_January_2015.JPG) | Martin Falbisoner | CC BY-SA 4.0 |
| `goreme.jpg` | [Panorama goreme.jpg](https://commons.wikimedia.org/wiki/File:Panorama_goreme.jpg) | Maliharehman | CC BY-SA 4.0 |
| `hadrian.jpg` | [Hadrian's Gate, Antalya 01.jpg](https://commons.wikimedia.org/wiki/File:Hadrian%27s_Gate,_Antalya_01.jpg) | Bernard Gagnon | CC BY-SA 3.0 |
| `kaleici.jpg` | [Antalya kaleiçi 2.jpg](https://commons.wikimedia.org/wiki/File:Antalya_kalei%C3%A7i_2.jpg) | REHBER0770 | CC BY-SA 4.0 |
| `konyaalti.jpg` | [Konyaaltı Beach, Antalya, Turkey 2022 Waiter.jpg](https://commons.wikimedia.org/wiki/File:Konyaalt%C4%B1_Beach,_Antalya,_Turkey_2022_Waiter.jpg) | Sharon Hahn Darlin | CC BY 2.0 |
| `kunefe.jpg` | [Knafeh From Yaffa Knafeh.jpg](https://commons.wikimedia.org/wiki/File:Knafeh_From_Yaffa_Knafeh.jpg) | Theipu | CC0 |
| `market.jpg` | [Bursa market Turkey 2013 2.jpg](https://commons.wikimedia.org/wiki/File:Bursa_market_Turkey_2013_2.jpg) | Karelj | CC BY-SA 3.0 |
| `redvalley.jpg` | [Cappadocia Goreme hike red valley badlands.jpg](https://commons.wikimedia.org/wiki/File:Cappadocia_Goreme_hike_red_valley_badlands.jpg) | Aquinoxmedia | CC BY-SA 4.0 |
| `rosevalley.jpg` | [Rose Valley, Cappadocia - Kızılçukur Vadisi, Kapadokya 08.jpg](https://commons.wikimedia.org/wiki/File:Rose_Valley,_Cappadocia_-_K%C4%B1z%C4%B1l%C3%A7ukur_Vadisi,_Kapadokya_08.jpg) | Zeynel Cebeci | CC BY-SA 4.0 |
| `simit.jpg` | [Simit-2x.JPG](https://commons.wikimedia.org/wiki/File:Simit-2x.JPG) | — | CC BY-SA 3.0 |
| `suluada.jpg` | [Adrasan Suluada.jpg](https://commons.wikimedia.org/wiki/File:Adrasan_Suluada.jpg) | Erturkercin | CC BY-SA 4.0 |
| `tea.jpg` | [Glass of tea 05119.jpg](https://commons.wikimedia.org/wiki/File:Glass_of_tea_05119.jpg) | Nevit Dilmen | CC BY-SA 3.0 |
| `testi.jpg` | [TestiKebabGoreme.jpg](https://commons.wikimedia.org/wiki/File:TestiKebabGoreme.jpg) | Niels Elgaard Larsen | CC BY-SA 3.0 |
| `uchisar.jpg` | [Castle Uçhisar in Cappadocia.jpg](https://commons.wikimedia.org/wiki/File:Castle_U%C3%A7hisar_in_Cappadocia.jpg) | This Photo was taken by Wolfgang Moroder.  

Feel free to use my photos, but ple | CC BY-SA 3.0 |

## 字体

Long Cang、Noto Sans SC、Noto Serif SC、Caveat、Pinyon Script、IBM Plex Mono，均为 [SIL Open Font License](https://openfontlicense.org) 开源字体，来自 [google/fonts](https://github.com/google/fonts)。

## 代码

页面代码、版式和线稿插画为本项目原创。
