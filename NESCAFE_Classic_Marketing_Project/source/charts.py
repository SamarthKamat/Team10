import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
RED='#B0161E'; BROWN='#4E342E'; ESP='#1F1410'; CREAM='#F4EBDD'; GOLD='#B8894A'; GREY='#7A6A62'; LIGHT='#D9C7B0'
plt.rcParams.update({'font.family':'Carlito','font.size':12,'axes.edgecolor':'#BFB2A6','axes.labelcolor':ESP,'xtick.color':GREY,'ytick.color':GREY})
def save(f,n): f.savefig(f'fig/{n}.png',dpi=220,bbox_inches='tight',facecolor='white'); plt.close(f)

# 1 e-commerce share
f,ax=plt.subplots(figsize=(7,3.4))
labs=['Urban India','All metros','Top-8 metros']; v=[6,14,18]
b=ax.barh(labs,v,color=[LIGHT,GOLD,RED],height=.55)
for r,x in zip(b,v): ax.text(x+.4,r.get_y()+r.get_height()/2,f'{x}%',va='center',color=ESP,fontsize=13,fontweight='bold')
ax.set_xlim(0,22); ax.invert_yaxis(); ax.spines[['top','right']].set_visible(False); ax.set_xlabel('E-commerce (incl. quick commerce) share of FMCG sales, Oct–Dec 2025 quarter')
ax.xaxis.grid(True,color='#EEE6DC'); ax.set_axisbelow(True)
save(f,'fig_ecom_share')

# 2 consumption
f,ax=plt.subplots(figsize=(5.5,3.4))
b=ax.bar(['2012','2023'],[84000,91000],color=[LIGHT,BROWN],width=.5)
for r,x in zip(b,[84000,91000]): ax.text(r.get_x()+r.get_width()/2,x+1500,f'{x:,} t',ha='center',color=ESP,fontsize=13,fontweight='bold')
ax.set_ylim(0,105000); ax.set_ylabel('Domestic coffee consumption (tonnes)'); ax.spines[['top','right']].set_visible(False)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x,p:f'{int(x/1000)}k'))
save(f,'fig_consumption')

# 3 nestle growth
f,ax=plt.subplots(figsize=(7,3.4))
q=['Q4 FY25\n(Jan–Mar 25)','Q4 FY26\n(Jan–Mar 26)','Q1 FY27\n(Apr–Jun 26)','Q2 FY27\n(Jul–Sep 26)']; v=[3.7,23.4,25.4,20.5]
b=ax.bar(q,v,color=[LIGHT,GOLD,RED,RED],width=.55)
for r,x in zip(b,v): ax.text(r.get_x()+r.get_width()/2,x+.6,f'{x}%',ha='center',color=ESP,fontsize=13,fontweight='bold')
ax.set_ylim(0,30); ax.set_ylabel('Total sales growth, y-o-y (%)'); ax.spines[['top','right']].set_visible(False)
save(f,'fig_nestle_growth')

# 4 perceptual map
f,ax=plt.subplots(figsize=(7.6,6))
ax.axhline(5,color='#CBBFB2',lw=1); ax.axvline(5,color='#CBBFB2',lw=1)
pts=[('NESCAFÉ Classic',6.3,7.4,RED,520),('NESCAFÉ Sunrise',3.6,5.2,'#D9686E',260),('NESCAFÉ Gold',8.5,8.7,'#7E0F15',260),
('BRU Instant',3.2,4.4,BROWN,380),('BRU Gold',6.9,6.9,'#7B5A4E',260),('Tata Coffee Grand',4.1,5.0,GOLD,300),
('Tata Coffee Grand Premium',6.2,6.3,'#D4A86A',240),('Continental Xtra',2.6,3.9,GREY,240),('Continental Speciale',5.2,5.9,'#A89A92',220),
('D2C specialty instant\n(e.g., Sleepy Owl, Rage)',8.9,7.6,ESP,260)]
lab={'NESCAFÉ Classic':(4.3,8.6),'NESCAFÉ Sunrise':(1.6,6.4),'NESCAFÉ Gold':(5.7,9.35),'BRU Instant':(1.3,4.65),'BRU Gold':(8.0,5.95),
'Tata Coffee Grand':(4.5,4.0),'Tata Coffee Grand Premium':(6.6,5.4),'Continental Xtra':(1.4,3.0),'Continental Speciale':(3.9,6.6),'D2C specialty instant\n(e.g., Sleepy Owl, Rage)':(7.75,6.95)}
for n,x,y,c,s in pts:
  ax.scatter(x,y,s=s,color=c,edgecolor='white',lw=1.5,zorder=3)
  lx,ly=lab[n]
  ax.annotate(n,xy=(x,y),xytext=(lx,ly),fontsize=12.5 if n=='NESCAFÉ Classic' else 10.5,fontweight='bold' if n=='NESCAFÉ Classic' else 'normal',color=ESP,
    arrowprops=dict(arrowstyle='-',color='#B9AC9F',lw=.8,shrinkB=7),va='center')
ax.set_xlim(1,10); ax.set_ylim(2,10); ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('Price positioning  →  (value  ……  premium)'); ax.set_ylabel('Perceived coffee quality / "coffee-forward" taste  →')
for t,x,y in [('Premium coffee-forward',9.8,9.75),('Value blends',1.15,2.2)]: ax.text(x,y,t,ha='right' if x>5 else 'left',va='top' if y>5 else 'bottom',fontsize=10,color=GREY,style='italic')
ax.spines[['top','right']].set_visible(False)
save(f,'fig_perceptual_map')

# helper box
def box(ax,x,y,w,h,txt,fc,tc='white',fs=11,bold=False):
  ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',fc=fc,ec='none'))
  ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold' if bold else 'normal',wrap=True)

# 5 STP flow
f,ax=plt.subplots(figsize=(10,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
cols=[(RED,'SEGMENTATION','Demographic · Geographic\nPsychographic · Behavioural\n→ 5 candidate segments'),(BROWN,'TARGETING','Primary: urban & semi-urban\nyoung adults (18–30)\nSecondary: working households\n& first-time coffee triers'),(ESP,'POSITIONING','"The everyday 100% pure\ncoffee that starts every\nambition" – aroma, energy,\nself-made youth')]
for i,(c,t,s) in enumerate(cols):
  x=.2+i*3.3; box(ax,x,2.55,2.9,.8,t,c,fs=14,bold=True); box(ax,x,.2,2.9,2.2,s,CREAM,ESP,fs=11.5)
  if i<2: ax.annotate('',xy=(x+3.25,2.95),xytext=(x+2.95,2.95),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=2.5))
save(f,'fig_stp')

# 6 product levels
f,ax=plt.subplots(figsize=(7,6)); ax.set_xlim(-3.3,3.3); ax.set_ylim(-3.1,3.1); ax.axis('off'); ax.set_aspect('equal')
for r,c in [(3,CREAM),(2.1,LIGHT),(0.95,RED)]: ax.add_patch(Circle((0,0),r,fc=c,ec='white',lw=3))
ax.text(0,0.12,'CORE',ha='center',color='white',fontweight='bold',fontsize=13); ax.text(0,-.3,'Quick energy &\ncoffee pleasure',ha='center',va='top',color='white',fontsize=9.5)
ax.text(0,1.72,'ACTUAL',ha='center',color=ESP,fontweight='bold',fontsize=12); ax.text(0,1.52,'100% pure soluble coffee · aroma · red-cap jar,\npouch & sachet · NESCAFÉ brand name',ha='center',va='top',color=ESP,fontsize=8.8)
ax.text(0,-1.38,'',ha='center')
ax.text(0,2.62,'AUGMENTED',ha='center',color=BROWN,fontweight='bold',fontsize=12); ax.text(0,-2.25,'Recipes & cold-coffee how-tos · wide availability\n(kirana → quick commerce) · Nestlé quality assurance\n· NESCAFÉ cafés/vending (Nestlé Professional)',ha='center',va='center',color=BROWN,fontsize=8.8)
save(f,'fig_product_levels')

# 7 channels
f,ax=plt.subplots(figsize=(10,4.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
box(ax,.2,1.8,1.9,1,'Nestlé India\nfactories',ESP,fs=12,bold=True)
box(ax,2.7,3.2,2.2,.9,'Distributors /\nre-distributors',BROWN,fs=11)
box(ax,2.7,1.85,2.2,.9,'Modern-trade &\nkey-account supply',BROWN,fs=11)
box(ax,2.7,.5,2.2,.9,'E-com & quick-com\n(dark stores, B2B)',BROWN,fs=11)
outs=[(3.55,'General trade: kiranas, wholesalers,\nrural stockists (~90% of FMCG volume)'),(2.2,'Modern trade: supermarkets &\nhypermarkets (e.g., chains, cash & carry)'),(.85,'Marketplaces & quick commerce:\nAmazon, Flipkart, BigBasket, Blinkit,\nZepto, Swiggy Instamart')]
for y,t in outs: box(ax,5.5,y-.35,3,1,t,CREAM,ESP,fs=10.2)
box(ax,8.7,1.6,1.15,1.4,'Consumer\n(home,\nhostel,\noffice)',RED,fs=11,bold=True)
for y in [3.65,2.3,.95]:
  ax.annotate('',xy=(2.7,y),xytext=(2.1,2.3),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=2))
  ax.annotate('',xy=(5.5,y+.0),xytext=(4.9,y),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=2))
  ax.annotate('',xy=(8.7,2.3),xytext=(8.5,y),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=1.5))
save(f,'fig_channels')

# 8 qual workflow
f,ax=plt.subplots(figsize=(10,2.4)); ax.set_xlim(0,10); ax.set_ylim(0,2.4); ax.axis('off')
st=['1. Design\nguide & consent','2. Purposive\nsample (n≥5)','3. Interview\n& record','4. Transcribe\nverbatim','5. In-vivo\ncoding','6. Categories\n→ themes','7. Insights &\nimplications']
for i,s in enumerate(st):
  x=.05+i*1.42; box(ax,x,.5,1.25,1.4,s,[RED,BROWN,ESP][i%3],fs=10.5,bold=False)
  if i<6: ax.annotate('',xy=(x+1.42,1.2),xytext=(x+1.27,1.2),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=2))
save(f,'fig_qual_workflow')

# 9 marketing plan gantt
f,ax=plt.subplots(figsize=(8.5,3.8))
acts=[('Shoppable “First-Cup Kit” on quick commerce',0,13,RED),('Campus “Make Your Mug” activation (10 cities)',3,9,BROWN),('Creator series: 30-second desk & hostel recipes',1,12,GOLD),('Kirana sachet-strip & POS refresh (Tier-2)',2,10,GREY),('UGC “Mug Stories” contest + retargeting',6,7,'#7E0F15'),('Measure, learn & scale',10,3,ESP)]
for i,(n,s,d,c) in enumerate(acts):
  ax.barh(i,d,left=s,color=c,height=.6); ax.text(-.2,i,n,ha='right',va='center',fontsize=12.5,color=ESP)
ax.set_yticks([]); ax.invert_yaxis(); ax.set_xlim(0,13); ax.set_xticks([0,4.33,8.67,13]); ax.set_xticklabels(['Week 1','Month 2','Month 3','Week 13'])
for x in [4.33,8.67]: ax.axvline(x,color='#DDD',lw=1,ls='--')
ax.spines[['top','right','left']].set_visible(False)
save(f,'fig_plan_gantt')
print('done')
