class finaldoutput:

    def __init__(self, name):
        self.name=name
        return

    def finaldoutputprocess(self,filteredGenelist23,filteredPoslist23,filtereddepthlist2up3,filteredAGlist13,filteredReflist23,filteredAltlist23,filteredAAlist213,filteredAAlist223,filteredAAPoslist123,filteredcodondepthlist23,filteredDP4list13,filteredAFlist13,filteredmutationlist13,
        filteredQDlist13,filteredSORlist13,filteredMQlist13,filteredMQRankSumlist13,filteredfilterscorelist13,filteredDescriptionlist13,filteredcandidateslist13,
        filteredreportablelist13):
        import pandas as pd

        d3 = {
            "Gene": filteredGenelist23,
            "BasePOS": filteredPoslist23,
            "BaseDepth": filtereddepthlist2up3,
            "Agreents": filteredAGlist13,
            "Ref": filteredReflist23,
            "Alt": filteredAltlist23,
            "AAref": filteredAAlist213,
            "AAalt": filteredAAlist223,
            "AAPOS": filteredAAPoslist123,
            "CodonCoverage": filteredcodondepthlist23,
            "VAF(DP4)": filteredDP4list13,
            "AF": filteredAFlist13,
            "Mutation": filteredmutationlist13,
            "QD": filteredQDlist13,
            "SOR": filteredSORlist13,
            "MQ": filteredMQlist13,
            "MQRankSum": filteredMQRankSumlist13,
            "Filter": filteredfilterscorelist13,
            "FilterDescription": filteredDescriptionlist13,
            "Candidates": filteredcandidateslist13,
            "Reportable": filteredreportablelist13,
        }
        df3 = pd.DataFrame(data=d3)
        # df.to_csv('snpreport4.csv', index=False,)
        df3 = df3.sort_values(df3.columns[0], ascending=False)
        df3.to_csv(
            self.name + ".csv",
            index=False,
        )