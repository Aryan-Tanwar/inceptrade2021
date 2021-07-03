import streamlit as st
import numpy as np

def main():

    st.title("INCEPTRADE")
    company = ["VIGYAAN LIMITED","RICKIARDO LABORATORIES","TABASSUM PAPER","MAEVA LIMITED","VIRAL LIFE","BAWKHER LIMITED","RULES"]
    company_choice = st.sidebar.selectbox("Select Company",company)

    if company_choice == "VIGYAAN LIMITED":
        st.header("VIGYAAN LIMITED")
        st.subheader("**Ticker**")
        st.write("VIGN")
        st.subheader("**Industry**")
        st.write("Information Technology")
        st.write("Vigyaan Ltd. is a leading provider of consulting-led integrated portfolio services to customers which are Telecom Equipment Manufacturers, Telecom Service Providers and IT Infrastructure Service Providers, Business Process Outsourcing Service Providers as well as Enterprise Solutions Services (BFSI, Retail & Logistics, Manufacturing, Energy and Utility (E&U), and Healthcare, Life Sciences, etc.) of Information Technology (IT) and IT-enabled services delivered through a network of multiple locations around the globe. It also provides comprehensive range of IT services, including IT enabled services, application development and maintenance, consulting and enterprise business solutions, extended engineering solutions and infrastructure management services to a diversified base of corporate customers in a wide range of industries including insurance, banking and financial services, manufacturing, telecommunications, transportation and engineering services.")
        st.write("Being a large-cap it is fairly well-positioned in the market, ranking in the top 10 IT firms in India. The company is debt-free and has a very good dividend pay-out of 50%")

        data = np.random.randn(10)
        st.line_chart(data)


    elif company_choice == "RICKIARDO LABORATORIES":
        st.header("RICKIARDO LABORATORIES")
        st.subheader("**Ticker**")
        st.write("RICK")
        st.subheader("**Industry**")
        st.write("Pharmaceutical")
        st.write("Rickiardo Laboratories, together with its subsidiaries, engages in the research, development, manufacture, and sale of medicines and active pharmaceutical ingredients (APIs) in India and internationally. The Generics APIs segment develops, manufactures, and sells APIs and advanced intermediates for anti-retroviral (ARV), oncology, hepatitis C, cardiovascular, antidiabetic, anti-asthmatic, gastroenterology, and ophthalmic therapeutic areas. The Generics FDF segment develops and manufactures oral solid formulations for ARVs, anti-diabetic, cardiovascular, proton pump inhibitors, and central nervous system. The Synthesis segment provides contract development and manufacturing services for pharmaceutical companies. The company also manufactures and sells specialty ingredients used in the nutraceutical, dietary supplements, and cosmeceutical products. In addition, it offers chemistry, IP development, business support, and related services to the pharmaceutical community. The company was incorporated in 2005 and is based in Cuttack, India.")

        data = np.random.randn(10)
        st.line_chart(data)

    elif company_choice == "TABASSUM PAPER":
        st.header("TABASSUM PAPER")
        st.subheader("**Ticker**")
        st.write("TABM")
        st.subheader("**Industry**")
        st.write("Paper")
        st.write("Tabassum Paper Limited is a paper manufacturing company. The Company's products/services include Paper and Paper board. The Company offers products under various categories, including coated paper and board, uncoated paper and board, packaging broad and office documentation. Its office documentation products include Bond, Ledge, Copier, etc. Its uncoated paper and board products include TABM Maplitho (SHB), TABM Cheque paper and TABM pulpboard. Its office documentation papers include photocopy and multi-purpose papers for use in desktop, inkjet and laser printers, fax machines, photocopiers and other devices. Its manufacturing units include Tabassum Paper Mills and Khargpur Mills.")

        data = np.random.randn(10)
        st.line_chart(data)

    elif company_choice == "MAEVA LIMITED":
        st.header("MAEVA LIMITED")
        st.subheader("**Ticker**")
        st.write("MEVA")
        st.subheader("**Industry**")
        st.write("Fibre, Chemicals, textile")
        st.write("Maeva Limited operates in fibre, pulp, chemicals, textile, fertilizers, and insulators businesses in India and internationally. The company operates through Viscose, Chemicals, Cement, Financial Services, and others segments. It provides viscose staple fiber, a man-made biodegradable fiber for use in apparels, home textiles, dress materials, knitted wear products, and non-woven applications; wood pulp products; viscose filament yarn, a natural fibre for manufacturing fabrics; and textile products, such as linen and wool. The company also offers various chemical products, including chlor-alkali and epoxy resin products; and fertilizers comprising neem-coated urea, soil and crop specific customised fertilizers, seeds, agrochemicals, and plant and soil health products under the Maeva Dharti brand name. In addition, it provides electrical insulators for transmission lines and substations, as well as equipment and railways. Further, the company offers grey cement; white cement under the Maeva Cement brand; ready mix concrete; and cement-based putty")

        data = np.random.randn(10)
        st.line_chart(data)

    elif company_choice == "VIRAL LIFE":
        st.header("VIRAL LIFE")
        st.subheader("**Ticker**")
        st.write("VIRL")
        st.subheader("**Industry**")
        st.write("Banking and Insurance")
        st.write("Viral Holding Limited, through its subsidiary, Viral Life Insurance Company Limited, provides life insurance products in India. The company offers a range of participating, non-participating, and linked products covering life insurance, pension, and health benefits, including riders for individual and group segments. Its products are distributed through individual and corporate agents, banks, brokers, and other channels. The company also engages in the treasury investment activities. Viral Holding Services Limited has a strategic bancassurance relationship with SBI Limited. Viral Holding Limited was incorporated in 1988 and is based in New Delhi, India.")
        st.write("The company has a debt-free balance sheet.")

        data = np.random.randn(10)
        st.line_chart(data)

    elif company_choice == "BAWKHER LIMITED":
        st.header("BAWKHER LIMITED")
        st.subheader("**Ticker**")
        st.write("BAKH")
        st.subheader("**Industry**")
        st.write("FMCG")
        st.write("Bawkher Limited, formerly Syed Bawkher Limited is an India-based holding company. The Company is engaged in the business activity of trading and manufacturing of cosmetics, toiletries and other personal care products. It is a fast-moving consumer goods (FMCG) company. The Company's products include Kailash Parbat Thanda Tel, Almond Drops Hair Oil, Amla and Jasmine Hair Oil, Oily Skin Face Wash, Herbal Scrub Soap, etc. The Company's brands are being sold through stockists and are available in retail outlets across the country. The Company has approximately eight production facilities, of which four units are situated in Uttrakhand (at Joshimat and Bhimtal), three units are situated in Jammu and Kashmir for manufacturing of various variants of hair oils and the other unit is located at Udaipur, Rajasthan.")

        data = np.random.randn(10)
        st.line_chart(data)

    elif company_choice == "RULES":
        st.header("RULES")
        st.write("1-All trades will be executed only at market price in Round 2.")
        st.write("2-Teams can sell at any premium they want in Round 3 but not at a discount.")
        st.write("3-There can be no barter of stocks in Round 3. Any such attempt will result in marking down of the teams.")
        st.write("4-Teams cannot have long as well as short positions in a stock at the same time.")
        st.write("5-When a team short sells, its wallet value doesn’t diminish. But the short sell amount has to be less than or equal to half the portfolio value.")
        st.write("6-The margin trading limit is at 45%.")
        st.write("7-There will be a margin call when market value of the position is 10% morethan margin provided.")
        st.write("8-Teams have to have 2 companies at all times in the portfolio (this doesn’t include companies short sold). No one company can comprise of 70% or more of the portfolio.")
        st.write("9-Trading halts if broker faces technical issues.")


if __name__ == '__main__':
     main()

