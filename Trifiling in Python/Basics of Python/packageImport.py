import package2.moduleB # to import a module from a different package do package.module


import newPackage.shipping


newPackage.shipping.calc_shipping() #module needed



#ORRR


from newPackage.shipping import calc_shipping, tax #can import multiple with commas

calc_shipping() #no obkect (module) needed
tax()


#OR


from newPackage import shipping


shipping.tax()
shipping.calc_shipping()