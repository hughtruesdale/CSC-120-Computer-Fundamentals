str = "e-waste parapgraph = The Global E-waste Monitor 2020 report found that the world dumped a record 53.6 million tonnes of e-waste last year  equivalent to the the weight of 350 cruise ships the size of the Queen Mary 2, or enough to form a line 125 kilometres long. That's an increase of 21 per cent in five years, the report said.Just 17.4 per cent of it was recycled, meaning that an estimated $57 billion worth of gold, silver, copper, platinum and other high-value, recoverable materials used as components were mostly dumped or burned rather than being collected for treatment and reuse.China, with 10.1 million tonnes, was the biggest contributor to e-waste, and the United States was second with 6.9 million tonnes. India, with 3.2 million tonnes, was third. Together these three countries accounted for nearly 38 per cent of the world's e-waste last year. The new report also predicts global e-waste discarded products with a battery or plug  will reach 74 million tonnes by 2030 almost a doubling of e-waste in just 16 years.E-waste is a health and environmental hazard because it contains toxic additives or hazardous substances such as mercury. While the overall damage done to the environment from all the unrecycled waste may be incalculable, the message from the report was conclusive. The way in which we produce, consume and dispose of e-waste is unsustainable. Global warming is just one issue cited by the report as it noted 98 million tonnes of carbon dioxide equivalents were released into the atmosphere as a result of inadequate recycling of undocumented refrigerators and air-conditioners.What is happening in India and China is symptomatic of a wider problem in developing countries where demand for goods like washing machines, refrigerators and air conditioners is rising rapidly"""
a = str.lower()
words = {

}
x = a.split()
for i in x:
    if i not in words:
        words[i] = 1
    else:
        words[i] += 1

print (words)
